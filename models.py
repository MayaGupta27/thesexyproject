from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Gene(db.Model):
    __tablename__ = "genes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rs_nums = db.relationship('RSNum', backref='gene', lazy = True)
    
    def __init__(self, name):
        self.name = name

class RSNum(db.Model):
    __tablename__ = "rsnums"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50))
    good_allele = db.Column(db.String(200))
    risk_allele = db.Column(db.String(200))
    gene_id = db.Column(db.Integer, db.ForeignKey('genes.id'))
    
    def __init__(self, number, good_allele, risk_allele, gene):
        self.number = number
        self.good_allele = good_llele
        self.risk_allele = risk_allele
        self.gene = gene
