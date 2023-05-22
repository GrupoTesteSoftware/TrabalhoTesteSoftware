from app import db
from app import models
from app.serializers import ProdutoSchema

from flask import Blueprint, jsonify, request
from json import dumps as jsondump
import app.response as response
import json
Produto = Blueprint('Produto', __name__)

# Parameters: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url

@Produto.route('/Produtos/', methods=['GET'])
def listar_todos_produtos():

    result = models.Produto.query.all()
    return ProdutoSchema(many=True).jsonify(result), 200

@Produto.route('/Produto/cadastrar', methods=['PUT'])
def cadastrar_produto():
    codigoBarras = None
    response_data = json.loads(request.data.decode())

    if 'nome' not in response_data:
        return response.bad_request("Para cadastrar um produto é preciso de um nome para ele")
    if 'idFornecedor' not in response_data:
        return response.bad_request("Para cadastrar um produto atrelar aum forneceedor")
    
    if  'codigoBarras' in response_data:    
        codigoBarras = response_data['codigoBarras']
    idFornecedor = response_data['idFornecedor']
    nome = response_data['nome']
    Produto_obj = models.Produto(
        nome=nome, 
        codigoBarras=codigoBarras,
        idFornecedor=idFornecedor

    )
    db.session.add(Produto_obj)
    db.session.commit()

    return response.success()
