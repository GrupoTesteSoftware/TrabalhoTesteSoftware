from app import ma
from app.models import FakeLead

from marshmallow import fields, validates, ValidationError

class FakeLeadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FakeLead
        load_instance = True

    company = fields.Str(required=True)
    contact = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Never send the id')