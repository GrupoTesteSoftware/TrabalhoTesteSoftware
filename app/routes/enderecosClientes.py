from app import db
from app import models
from app.serializers import EnderecosClienteSchema


from datetime import datetime
from flask import Blueprint, jsonify, request
from json import dumps as jsondump
import json
import app.response as response

enderecoscliente = Blueprint('enderecoscliente', __name__)

@enderecoscliente.route('/cliente/<idCliente>/enderecos', methods=['GET'])
def listarEnderecosCliente(idCliente):
    result = models.EnderecosCliente.query.filter_by(idCliente=idCliente).all()
    return EnderecosClienteSchema(many=True).jsonify(result), 200

@enderecoscliente.route('/cliente/<idCliente>/endereco', methods=['PUT'])
def cadastrarEnderecoCliente(idCliente):
    response_data = json.loads(request.data.decode())

    cep = response_data['CEP']
    estado = response_data['estado']
    cidade = response_data['cidade']
    logradouro = response_data['logradouro']
    numero = response_data['numero']

    enderecoCliente_obj = models.EnderecosCliente(
        idCliente = idCliente,
        CEP = cep,
        estado = estado,
        cidade = cidade,
        logradouro = logradouro,
        numero = numero
    )

    db.session.add(enderecoCliente_obj)
    db.session.commit()
   
    return  response.success()