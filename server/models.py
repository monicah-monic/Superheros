from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
     __tablename__ = 'heros'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)
     super_name = db.Column(db.String)

     hero_powers =db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates= 'power', cascade='all, delete-orphan')

    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description)<20:
            raise ValueError("Description must be present and at least 20 characters long")
        return description

     

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))
    power_id = db.Column(db.interger,db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        values = ['Strong', 'Weak', 'Average']
        if strength not in values:
            raise ValueError("strength must be one of the following values: 'Strong', 'Weak', 'Average'")
        return strength