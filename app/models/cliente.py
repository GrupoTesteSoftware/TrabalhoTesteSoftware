from .rdb import db

class Cliente(db.Model):

    __tablename__ = 'clientes'  # Real table name, since is case sensitive

    id = db.Column(db.Integer, primary_key=True)
    CPF_CNPJ = db.Column(db.String,nullable=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    telefone = db.Column(db.String, nullable=True)
    tipo = db.Column(db.String, nullable=True)
    celular = db.Column(db.String, nullable=True)
    data = db.Column(db.DateTime, nullable=True)
    dataNascimento = db.Column(db.DateTime, nullable=True)

    def __init__(
                self,
                nome,
                CPF_CNPJ=None,
                email=None,
                telefone=None,
                tipo=None,
                celular=None,
                data=None,
                dataNascimento=None
            ):
        """Constructor to help write data"""

        self.nome = nome
        self.CPF_CNPJ = CPF_CNPJ
        self.email = email
        self.telefone = telefone
        self.tipo = tipo
        self.celular = celular
        self.data = data
        self.dataNascimento = dataNascimento

    def __repr__(self) -> str:
        """Object representation"""
        return self.nome
