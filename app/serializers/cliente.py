from app import ma
from app.models import Cliente

from marshmallow import fields, validates, ValidationError

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        load_instance = True

    CPF_CNPJ = fields.Str(required=False)
    nome = fields.Str(required=True)
    email = fields.Str(required=False)
    telefone = fields.Str(required=False)
    tipo = fields.Str(required=False)
    celular = fields.Str(required=False)
    data = fields.Str(required=False)
    dataNascimento = fields.Str(required=False)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Never send the id')