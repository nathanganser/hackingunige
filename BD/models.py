from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Bombardier(db.Model):
    __tablename__ = "Bombardier"
    id = db.Column(db.Integer, primary_key=True)
    nom_classe = db.Column(db.String)
    longueur = db.Column(db.Integer)
    prix = db.Column(db.Integer)
    equipage = db.Column(db.Integer)
    boucliers = db.Column(db.Integer)
    MGLT = db.Column(db.String)
    hyperdrive_classe = db.Column(db.Integer)
    classe_id = db.Column(db.Integer)
    constructeur_id = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Constructeur(db.Model):
    __tablename__ = "constructeur"
    id = db.Column(db.Integer, primary_key=True)
    nom_constructeur = db.Column(db.String)
    planete_constructeur = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Planete(db.Model):
    __tablename__ = "planete"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    type = db.Column(db.Integer)
    region = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class PlaneteType(db.Model):
    __tablename__ = "planete_type"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
