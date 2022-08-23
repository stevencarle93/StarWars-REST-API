"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets ))
    print(planets)
    return jsonify(planets), 200

@app.route('/planet/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if isinstance(planet, Planet):
        return jsonify(planet.internal()), 200
    else:
        return jsonify({
            "message":"planeta no encontrado"
        })

@app.route('/planet', methods=['POST'])
def register_planet():
    """
    Función con método POST
    """
    planet = Planet()
    body = request.json
    
    planet.climate = body["climate"]
    planet.created = body["created"]
    planet.diameter= body["diameter"]
    planet.gravity = body["gravity"]
    planet.name =body["name"]
    planet.orbital_period = body["orbital_period"]

    db.session.add(planet)
    try:        
        db.session.commit()
        return jsonify(planet.serialize()), 201
    except Exception as error:
        print(error)
        db.session.rollback()
        return jsonify({"message":"error"}), 400



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
