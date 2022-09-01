from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    def __repr__(self):
        return '<User %r>' % self.username

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    gravity = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period
        }

    def __repr__(self):  ##como se muestra al hacer print()
        return '<Planet %r>' % self.name

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    height = db.Column(db.Integer, nullable = False)
    mass = db.Column(db.Integer, nullable = False)
    hairColor = db.Column(db.String(250), nullable = False)
    skinColor = db.Column(db.String(250), nullable = False)

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hairColor": self.hairColor,
            "skinColor": self.skinColor
        }

    def __repr__(self):
        return '<People %r>' % self.name