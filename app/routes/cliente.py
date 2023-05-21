# cliente routes
from app import db
from app import models
from app.serializers import ClienteSchema


from datetime import datetime
from flask import Blueprint, jsonify, request
from json import dumps as jsondump
import json

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


@cliente.route('/cliente/pessoa', methods=['GET'])
def retrieve_pessoa_clientes():
    result = models.Cliente.query.filter_by(tipo='Pessoa' ).all()
    return ClienteSchema(many=True).jsonify(result), 200

@cliente.route('/cliente/pessoa/celular=<celular>', methods=['GET'])
def retrieve_pessoa_celular_clientes(celular):
    result = models.Cliente.query.filter_by(tipo='Pessoa' , celular=celular).all()
    return ClienteSchema(many=True).jsonify(result), 200

@cliente.route('/cliente/empresa/celular=<celular>', methods=['GET'])
def retrieve_empresa_celular_clientes(celular):
    result = models.Cliente.query.filter_by(tipo='Empresa' , celular=celular).all()
    return ClienteSchema(many=True).jsonify(result), 200


def js_to_py_datetime(str_datetime: str):
    str_datetime = str_datetime.replace('.000Z', '')
    return datetime.strptime(str_datetime, '%Y-%m-%d')

@cliente.route('/cliente/', methods=['POST'])
def create_cliente():
    """Create post cliente"""
    response_data = json.loads(request.data.decode())

    id = response_data['id']
    nome = response_data['nome']
    email = response_data['email']
    telefone = response_data['telefone']
    tipo = response_data['tipo']
    celular = response_data['celular']
    data = js_to_py_datetime(response_data['data'])
    dataNascimento = js_to_py_datetime(response_data['dataNascimento'])

    if int(id) == -1:
        cliente_obj = models.Cliente(
            nome = nome,
            email = email,
            telefone = telefone,
            tipo = tipo,
            celular = celular,
            data = data,
            dataNascimento = dataNascimento
        )

        db.session.add(cliente_obj)
    else:
        cliente_obj = models.Cliente.query.filter_by(id=id).first()

        setattr(cliente_obj, 'nome', nome)
        setattr(cliente_obj, 'email', email)
        setattr(cliente_obj, 'telefone', telefone)
        setattr(cliente_obj, 'tipo', tipo)
        setattr(cliente_obj, 'celular', int(celular))
        setattr(cliente_obj, 'data', data)
        setattr(cliente_obj, 'dataNascimento', dataNascimento)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@cliente.route('/cliente/<id>/atualizar', methods=['PATCH'])
def atualizar_Cadastro_Cliente(id):
    cpf_cnpj = None
    data = None
    dataNascimento = None
    

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

    
    if "data" in response_data:
        data = js_to_py_datetime(response_data['data'])
    
        
    if "dataNascimento" in response_data:
        dataNascimento = js_to_py_datetime(response_data['dataNascimento'])
        
    cliente_obj = models.Cliente.query.filter_by(id=id).first()
    
    setattr(cliente_obj, 'nome', nome)
    setattr(cliente_obj, 'email', email)
    setattr(cliente_obj, 'telefone', telefone)
    setattr(cliente_obj, 'tipo', tipo)
    setattr(cliente_obj, 'data', data)
    setattr(cliente_obj, 'dataNascimento', dataNascimento)
    setattr(cliente_obj, 'CPF_CNPJ', cpf_cnpj)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@cliente.route('/cliente/cadastrar', methods=['PUT'])
def cadastrar_cliente():
    cpf_cnpj = None
    data = None
    dataNascimento = None

    response_data = json.loads(request.data.decode())
    if 'CPF_CNPJ' in response_data:
        cpf_cnpj = response_data['CPF_CNPJ']
   
    nome = response_data['nome']
    email = response_data['email']
    telefone = response_data['telefone']
    tipo = response_data['tipo']
    celular = response_data['celular']
    if "data" in response_data:
        data = js_to_py_datetime(response_data['data'])
        
    if "dataNascimento" in response_data:
        dataNascimento = js_to_py_datetime(response_data['dataNascimento'])
 
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
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code



@cliente.route('/cliente/update/', methods=['POST'])
def update_cliente():
    """Update post cliente"""
    id = request.form['id']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    tipo = request.form['tipo']
    celular = request.form['celular']
    data = request.form['data']
    dataNascimento = request.form['dataNascimento']

    cliente_obj = models.Cliente.query.filter_by(id=id).first()

    setattr(cliente_obj, 'nome', nome)
    setattr(cliente_obj, 'email', email)
    setattr(cliente_obj, 'telefone', telefone)
    setattr(cliente_obj, 'tipo', tipo)
    setattr(cliente_obj, 'celular', int(celular))
    setattr(cliente_obj, 'data', data)
    setattr(cliente_obj, 'dataNascimento', dataNascimento)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

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
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code



@cliente.route('/cliente/<nome>', methods=['GET'])
def create_get_cliente(nome):
    """Create get cliente"""
    cliente_obj = models.Cliente( 
        nome=nome
    )

    db.session.add(cliente_obj)
    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@cliente.route('/cliente/update/<id>/<key>/<value>', methods=['GET'])
def update_get_cliente_column(id, key, value):
    """Update get cliente column"""

    cliente_obj = models.Cliente.query.filter_by(id=id).first()

    if key == "celular":
        value = int(value)

    setattr(cliente_obj, key, value)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code
