# cliente routes
from app import db
from app import models
from app.serializers import ClienteSchema
from datetime import datetime
from flask import Blueprint, jsonify, request
from json import dumps as jsondump
import json
import Packages.validadores as validadores
import app.response as response
import app.pipelineValidacoes as pipelineValidacoes

cliente = Blueprint('cliente', __name__)

# Parameters: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url

@cliente.route('/clientes/', methods=['GET'])
def retrieve_all_clientes():
    """Retrieve cliente"""
    '''
    id  = request.args.get('id', None)
    empresa  = request.args.get('empresa', None)
    nome  = request.args.get('nome', None)

    if not id and not empresa and not nome:
        response = models.cliente.query.all()
    elif not empresa and not nome:
        response = models.cliente.query.filter_by(id=id).first()
    '''
    result = models.Cliente.query.all()
    return ClienteSchema(many=True).jsonify(result), 200

@cliente.route('/cliente/empresa', methods=['GET'])
def retrieve_empresa_clientes():
    result = models.Cliente.query.filter_by(tipo='Empresa' ).all()
    return ClienteSchema(many=True).jsonify(result), 200


@cliente.route('/cliente/pessoaFisica', methods=['GET'])
def retrieve_pessoa_clientes():
    result = models.Cliente.query.filter_by(tipo='Pessoa' ).all()
    return ClienteSchema(many=True).jsonify(result), 200

def js_to_py_datetime(str_datetime: str):
    str_datetime = str_datetime.replace('.000Z', '')
    return datetime.strptime(str_datetime, '%Y-%m-%d')

@cliente.route('/cliente/<id>/atualizar', methods=['PATCH'])
def atualizar_Cadastro_Cliente(id):
    cpf_cnpj = None
    data = None
    dataNascimento = None
    celular = None
    nome = None

    response_data = json.loads(request.data.decode())
    if 'CPF_CNPJ' in response_data:
        cpf_cnpj = response_data['CPF_CNPJ'] 
    if  'nome' in response_data:    
        nome = response_data['nome']
    if 'email' in  response_data:
        email = response_data['email']
    if 'telefone' in response_data:
        telefone = response_data['telefone']
    if 'tipo' in response_data:
        tipo = response_data['tipo']
    if 'data' in response_data:
        data = js_to_py_datetime(response_data['data'])
    if 'dataNascimento' in response_data:
        dataNascimento = js_to_py_datetime(response_data['dataNascimento'])
    if 'celular' in response_data:
        celular = response_data['celular']
    
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            (validadores.validarCPF_CNPJ(cpf_cnpj,tipo), "CPF ou CNPJ invalido."),
            (validadores.validarEmail(email), "Email Invalido"),
            (validadores.validarTelefoneFixo(telefone), "Telefone Fixo Invalido"),
            (validadores.validarData(dataNascimento), "Data de nascimento Invalida"),
            (validadores.validarCelular(celular), "Celular Invalido")
        ]
    )
    if resultado is False: 
        return response.bad_request(mensagem)
    
    cliente_obj = models.Cliente.query.filter_by(id=id).first()
    if cliente_obj is None:
        return response.bad_request("Cliente Nao Encontrado")

    
    setattr(cliente_obj, 'nome', nome)
    setattr(cliente_obj, 'email', email)
    setattr(cliente_obj, 'telefone', telefone)
    setattr(cliente_obj, 'tipo', tipo)
    setattr(cliente_obj, 'data', data)
    setattr(cliente_obj, 'dataNascimento', dataNascimento)
    setattr(cliente_obj, 'CPF_CNPJ', cpf_cnpj)

    db.session.commit()
    
    return response.success()

@cliente.route('/cliente/cadastrar', methods=['PUT'])
def cadastrar_cliente():
    cpf_cnpj = None
    data = None
    dataNascimento = None
    celular = None

    response_data = json.loads(request.data.decode())
    if 'nome' not in response_data:
        return response.bad_request("Para cadastrar um cliente é preciso de um nome")

    if 'CPF_CNPJ' in response_data:
        cpf_cnpj = response_data['CPF_CNPJ']
    
       
    nome = response_data['nome']
    email = response_data['email']
    telefone = response_data['telefone']
    tipo = response_data['tipo']
    if 'celular' in response_data:
        celular = response_data['celular']
    if "data" in response_data:
        data = js_to_py_datetime(response_data['data'])
        
    if "dataNascimento" in response_data:
        dataNascimento = js_to_py_datetime(response_data['dataNascimento'])
 
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            (validadores.validarCPF_CNPJ(cpf_cnpj,tipo), "CPF ou CNPJ invalido."),
            (validadores.validarEmail(email), "Email Invalido"),
            (validadores.validarTelefoneFixo(telefone), "Telefone Fixo Invalido"),
            (validadores.validarData(dataNascimento), "Data de nascimento Invalida"),
            (validadores.validarCelular(celular), "Celular Invalido")
        ]
    )

    if  models.Cliente.query.filter_by(CPF_CNPJ=cpf_cnpj).first():
        return response.bad_request("Ja existe um usario com esse CPF/CNPJ")
    
    if resultado is False: 
        return response.bad_request(mensagem)

    cliente_obj = models.Cliente(
        CPF_CNPJ = cpf_cnpj,
        nome = nome,
        email = email,
        telefone = telefone,
        tipo = tipo,
        celular = celular,
        data = data,
        dataNascimento = dataNascimento
    )

    db.session.add(cliente_obj)

    db.session.commit()
    
    return response.success({"idCliente":cliente_obj.id})



@cliente.route('/cliente/update_column/', methods=['POST'])
def update_cliente_column():
    """Update post cliente column"""
    id = request.form['id']
    key = request.form['key']
    value = request.form['value']

    cliente_obj = models.Cliente.query.filter_by(id=id).first()

    if key == "celular":
        value = int(value)

    setattr(cliente_obj, key, value)

    db.session.commit()
    return response.success()