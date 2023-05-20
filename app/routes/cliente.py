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

@cliente.route('/cliente/', methods=['GET'])
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

@cliente.route('/cliente/pessoa/etapa=<etapa>', methods=['GET'])
def retrieve_pessoa_etapa_clientes(etapa):
    result = models.Cliente.query.filter_by(tipo='Pessoa' , etapa=etapa).all()
    return ClienteSchema(many=True).jsonify(result), 200

@cliente.route('/cliente/empresa/etapa=<etapa>', methods=['GET'])
def retrieve_empresa_etapa_clientes(etapa):
    result = models.Cliente.query.filter_by(tipo='Empresa' , etapa=etapa).all()
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
    etapa = response_data['etapa']
    data = js_to_py_datetime(response_data['data'])
    expectativa = js_to_py_datetime(response_data['expectativa'])

    if int(id) == -1:
        cliente_obj = models.Cliente(
            nome = nome,
            email = email,
            telefone = telefone,
            tipo = tipo,
            etapa = etapa,
            data = data,
            expectativa = expectativa
        )

        db.session.add(cliente_obj)
    else:
        cliente_obj = models.Cliente.query.filter_by(id=id).first()

        setattr(cliente_obj, 'nome', nome)
        setattr(cliente_obj, 'email', email)
        setattr(cliente_obj, 'telefone', telefone)
        setattr(cliente_obj, 'tipo', tipo)
        setattr(cliente_obj, 'etapa', int(etapa))
        setattr(cliente_obj, 'data', data)
        setattr(cliente_obj, 'expectativa', expectativa)

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
    etapa = request.form['etapa']
    data = request.form['data']
    expectativa = request.form['expectativa']

    cliente_obj = models.Cliente.query.filter_by(id=id).first()

    setattr(cliente_obj, 'nome', nome)
    setattr(cliente_obj, 'email', email)
    setattr(cliente_obj, 'telefone', telefone)
    setattr(cliente_obj, 'tipo', tipo)
    setattr(cliente_obj, 'etapa', int(etapa))
    setattr(cliente_obj, 'data', data)
    setattr(cliente_obj, 'expectativa', expectativa)

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

    if key == "etapa":
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

    if key == "etapa":
        value = int(value)

    setattr(cliente_obj, key, value)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code
