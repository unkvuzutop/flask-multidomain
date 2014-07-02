from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, UniqueConstraint
from flsktest import db

class ModelDomain(db.Model):
    id = Column(Integer, primary_key=True)
    domain = Column(String(120))
    domain_type = Column(String(10))

    __tablename__ = 'model_domains'
    __table_args__ = (UniqueConstraint('domain', 'domain_type', name='_domain_domain_type_uc'),)

    def __init__(self, domain=None, domain_type=None):
        self.domain = domain
        self.domain_type = domain_type

    def __repr__(self):
        return '<Domain %r %r>' % (self.domain, self.domain_type)