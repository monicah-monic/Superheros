from flask import Flask,request,jsonify, make_response
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///superheros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h2> SUPERHEROS: GET/POST/PATCH/DELETE </h2>'

@app.route('/heros', methods=['GET'])
def get_heros():
    heros= Hero.query.all()
    return jsonify([
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
        } 
        for hero in heros
        ])






@app.route('/powers', methods=['GET'])
def get_powers():
    powers= Power.query.all()
    return jsonify([
        {
            "description": power.description,
            "id":power.id,
            "name": power.name,
        
        } 
        for power in powers
        ])

@app.route('/powers/<int:id>', methods=['GET'])
def get_powers_by_id(id):
    try:
        power = Power.query.get(id)
        return jsonify([
            {
                "description": power.description,
                "id":power.id,
                "name": power.name
            }
        ])
    except Exception as e:
        print(f"Power not found: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)
    
    
# @app.route('/heros/<int:id>', methods=['GET'])
# def get_heros_by_id(id):
#     hero = Hero.query.get(id)
#     try:
#        if hero:
#         return jsonify
   








if __name__ == '__main__':
    app.run(port=5555, debug=True)
