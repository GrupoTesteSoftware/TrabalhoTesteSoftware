from .rdb import db

class FakeLead(db.Model):

    __tablename__ = 'fake_lead'  # Real table name, since is case sensitive

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String, nullable=True)
    company = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    def __init__(self, contact, company) -> None:
        """Constructor to help write data"""
        self.contact = contact
        self.company = company

    def __repr__(self) -> str:
        """Object representation"""
        return self.company
