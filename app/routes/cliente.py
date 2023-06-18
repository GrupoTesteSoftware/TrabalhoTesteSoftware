from app import db
from app import models
from app.serializers import ClienteSchema
from datetime import datetime
from flask import Blueprint, jsonify, request,abort
from json import dumps as jsondump
import json
import packages.validadores as validadores
import app.response as response
import app.pipelineValidacoes as pipelineValidacoes
from flask_restx import Api, Namespace, Resource, fields
from datetime import datetime


cliente = Blueprint('cliente', __name__)


nsCliente = Namespace("cliente",  description="Operação Com Clientes")

cliente_model = nsCliente.model('Cliente', {
    'CPF_CNPJ': fields.String(required=False, description="identificador de Cliente PF ou PJ"),
    'nome': fields.String(required=True, description="Nome cliente"),
    'email': fields.String(required=False, description="endereco de email"),
    'telefone': fields.String(required=False,description="telefone"),
    'whatsapp': fields.String(required=False,description="whatsapp para contato"),
    'celular': fields.String(required=False,description="User's name"),
    'dataNascimento': fields.String(required=False,description="User's name"),
})


# ROTAS 
@nsCliente.route("/listarTodos",methods=['GET'])
class ClienteResource(Resource):
    def get(self):
        return listarTodosClientes()
    
@nsCliente.route('/listarPessoaJuridica',methods=['GET'])
class ClienteResource(Resource):
    def get(self):
        return listarPessoaJuridica()

@nsCliente.route('/cliente/listarPessoaFisica', methods=['GET'])
class ClienteResource(Resource):
    def get(self):
        return listarPessoaFisica()
    
@nsCliente.route('/<id>/atualizar', methods=['PATCH'])
class ClienteResource(Resource):
    @nsCliente.expect(cliente_model, validate=True)
    def patch(self,id):
        return atualizarCadastroCliente(id)
@nsCliente.route('/cadastrar', methods=['PUT'])
class ClienteResource(Resource):
    @nsCliente.expect(cliente_model, validate=True)
    def put(self):
        return cadastrarCliente()
  
@nsCliente.route('/<id>/deletar', methods=['DELETE'])
class ClienteResource(Resource):
    def delete(self,id):
        return deletarCliente(id)  
    
# @cliente.route('/cliente/update_column/', methods=['POST'])
# def update_cliente_column():
#     """Update post cliente column"""
#     id = request.form['id']
#     key = request.form['key']
#     value = request.form['value']

#     cliente_obj = models.Cliente.query.filter_by(id=id).first()

#     if key == "celular":
#         value = int(value)

#     setattr(cliente_obj, key, value)

#     db.session.commit()
#     return response.success()




#Funcoes

def listarTodosClientes():
    result = models.Cliente.query.all()
    return ClienteSchema(many=True).jsonify(result)

def listarPessoaJuridica():
    result = models.Cliente.query.filter_by(whatsapp='Empresa' ).all()
    return ClienteSchema(many=True).jsonify(result)

def listarPessoaFisica():
    result = models.Cliente.query.filter_by(whatsapp='Pessoa' ).all()
    return ClienteSchema(many=True).jsonify(result)

def atualizarCadastroCliente(id):
    cpf_cnpj = None
    dataExlusao = None
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
    if 'whatsapp' in response_data:
        whatsapp = response_data['whatsapp']
    if 'dataNascimento' in response_data:
        dataNascimento = response_data['dataNascimento']
    if 'celular' in response_data:
        celular = response_data['celular']
    
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            (validadores.validarCPF_CNPJ(cpf_cnpj,whatsapp), "CPF ou CNPJ invalido."),
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
    setattr(cliente_obj, 'whatsapp', whatsapp)
    setattr(cliente_obj, 'data', dataExlusao)
    setattr(cliente_obj, 'dataNascimento',  datetime.strptime(dataNascimento, "%Y-%m-%d"))
    setattr(cliente_obj, 'CPF_CNPJ', cpf_cnpj)

    db.session.commit()
    
    return response.success()

def cadastrarCliente():
    cpf_cnpj = None
    dataNascimento = None
    celular = None
    telefone = None

    response_data = json.loads(request.data.decode())
    if 'nome' not in response_data:
        return response.bad_request("Para cadastrar um cliente é preciso de um nome")

    if 'CPF_CNPJ' in response_data:
        cpf_cnpj = response_data['CPF_CNPJ']
    
       
    nome = response_data['nome']
    email = response_data['email']
    if 'email' in response_data:
        email = response_data['email']
    if 'telefone' in response_data:
        telefone = response_data['telefone']
    if 'whatsapp' in response_data:
        whatsapp = response_data['whatsapp']
    if 'celular' in response_data:
        celular = response_data['celular']
    if "dataNascimento" in response_data:
        dataNascimento = response_data['dataNascimento']
 
    resultado,mensagem = pipelineValidacoes.Executar(
        [
            (validadores.validarCPF_CNPJ(cpf_cnpj), "CPF ou CNPJ invalido."),
            (validadores.validarEmail(email), "Email Invalido"),
            (validadores.validarTelefoneFixo(telefone), "Telefone Fixo Invalido"),
            (validadores.validarData(dataNascimento), "Data de nascimento Invalida"),
            (validadores.validarCelular(celular), "Celular Invalido")
        ]
    )

    if  models.Cliente.query.filter_by(CPF_CNPJ=cpf_cnpj).first():
        codigo, mensagem = response.bad_request("Ja existe um usario com esse CPF/CNPJ")
        abort(codigo, mensagem)
    
    if resultado is False: 
        codigo, mensagem = response.bad_request(mensagem)
        abort(codigo, mensagem)

    cliente_obj = models.Cliente(
        CPF_CNPJ = cpf_cnpj,
        nome = nome,
        email = email,
        telefone = telefone,
        whatsapp = whatsapp,
        celular = celular,
        dataNascimento =  datetime.strptime(dataNascimento, "%Y-%m-%d")
    )

    db.session.add(cliente_obj)

    db.session.commit()
    
    return {'id':cliente_obj.id}

def deletarCliente(id):
    cliente_obj = models.Cliente.query.filter_by(id=id).first()
    if cliente_obj is None:
        codigo, mensagem = response.bad_request("Cliente Nao Encontrado")
        abort(codigo, mensagem)
    dataExlusao =  datetime.now()
    setattr(cliente_obj, 'dataExlusao', dataExlusao)
    db.session.commit()
    return True
    