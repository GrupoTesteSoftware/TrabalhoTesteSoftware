# Fake Lead routes
from app import db
from app import models
from app.serializers import FakeLeadSchema

from flask import Blueprint, jsonify, request
from json import dumps as jsondump

fake_lead = Blueprint('fake_lead', __name__)

# Parameters: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url

@fake_lead.route('/fake/', methods=['GET'])
def retrieve_all_fake_leads():
    """Retrieve fake"""
    '''
    id  = request.args.get('id', None)
    contact  = request.args.get('contact', None)
    company  = request.args.get('company', None)

    if not id and not contact and not company:
        response = models.FakeLead.query.all()
    elif not contact and not company:
        response = models.FakeLead.query.filter_by(id=id).first()
    '''
    result = models.FakeLead.query.all()
    return FakeLeadSchema(many=True).jsonify(result), 200

@fake_lead.route('/fake/', methods=['POST'])
def create_fake():
    """Create post fake"""
    contact = request.form['contact']
    company = request.form['company']
    fake_obj = models.FakeLead(
        contact=contact, 
        company=company
    )

    db.session.add(fake_obj)
    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code


@fake_lead.route('/fake/<company>/<contact>', methods=['GET'])
def create_get_fake(company, contact):
    """Create get fake"""
    fake_obj = models.FakeLead(
        contact=contact, 
        company=company
    )

    db.session.add(fake_obj)
    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code
