from flask import  jsonify


def success(data:dict = None):
    response = {
        'success': True,
        'message': 'Operation successful',
        'data': data
     }
    return jsonify(response), 200


def bad_request(messagem: str):
    response = {
        'success': False,
        'message': 'Bad request: ' + + messagem
    }
    return jsonify(response), 400


def unauthorized(messagem : str):
    response = {
        'success': False,
        'message': 'Unauthorized: ' + + messagem
    }
    return jsonify(response), 401


def not_found(messagem : str):
    response = {
        'success': False,
        'message': 'Resource not found: ' + messagem
    }
    return jsonify(response), 404


def internal_server_error(messagem: str):
    response = {
        'success': False,
        'message': 'Internal server error: '+ messagem
    }
    return jsonify(response), 500