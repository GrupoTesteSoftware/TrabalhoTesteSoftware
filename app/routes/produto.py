from app import db
from app import models
from app.serializers import ProdutoSchema

from flask import Blueprint, jsonify, request
from json import dumps as jsondump
import app.response as response

Produto = Blueprint('Produto', __name__)

# Parameters: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url

@Produto.route('/Produtos/', methods=['GET'])
def retrieve_all_Produtos():
    """Retrieve Produto"""
    '''
    id  = request.args.get('id', None)
    contact  = request.args.get('contact', None)
    company  = request.args.get('company', None)

    if not id and not contact and not company:
        response = models.Produto.query.all()
    elif not contact and not company:
        response = models.Produto.query.filter_by(id=id).first()
    '''
    result = models.Produto.query.all()
    return ProdutoSchema(many=True).jsonify(result), 200

@Produto.route('/Produto/', methods=['PUT'])
def cadasttar_Produto():
    """Create post Produto"""
    contact = request.form['contact']
    company = request.form['company']
    Produto_obj = models.Produto(
        contact=contact, 
        company=company
    )

    db.session.add(Produto_obj)
    db.session.commit()

    return response.success()
