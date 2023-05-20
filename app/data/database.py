"""Compile of useful fuctions to manage database"""

import json
import os
from app.models import Cliente
from app.models import FakeLead
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

def verify_cliente_is_populated(db) -> bool:
    """Verify if cliente is populated already"""
    Session = sessionmaker(bind=db.engine)
    session = Session()
    response = session.execute(text(" SELECT * FROM clientes LIMIT 1"))
    return not response.fetchall()

def populate_database(db):
    """Populate cliente table."""
    with open(
        os.path.join(
            os.path.dirname(__file__),
            'initial_cliente.json'
            )
        ) as json_file:
        clientes = json.load(json_file)
    for cliente in clientes:
        query = (
            "INSERT OR IGNORE INTO cliente" 
            "   (nome, email, telefone, tipo, etapa, data, dataNascimento) "
            "VALUES "
            f"('{cliente['nome']}', '{cliente['email']}', '{cliente['telefone']}', "
            f"'{cliente['tipo']}', '{cliente['etapa']}', "
            f"'{cliente['data'] + '00:00:00'}', "
            f"'{cliente['dataNascimento'] + '00:00:00'}')"
        )
        db.engine.execute(query)
