from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy



# Here, you create an instance of the Flask class. 
# The __name__ argument is passed to the Flask class to tell the instance where to look for resources like templates and static files. 
# __name__ is a special variable in Python that holds the name of the current module, 
# which is useful for Flask to determine the root path of the application.
app = Flask(__name__)
# SQL lite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
db = SQLAlchemy(app)

# Inheriting from db.Model makes this class a model in SQLAlchemy, 
# meaning it maps to a table in the database.
class Drink(db.Model):
    # Each class attribute represents a column in the corresponding database table.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"



#@app.route('/') tells Flask to execute the index function whenever a user navigates to the root URL ('/') of the application.
@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {'name': drink.name, 'decription': drink.description}
        output.append(drink_data)
    return {"drink": output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name = request.json['name'], 
                  description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink():
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "Drink not Found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Drink deleted successfully!"}

@app.route('/drinks/<id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get_or_404(id)
    if 'name' in request.json:
        drink.name = request.json['name']
    if 'description' in request.json:
        drink.description = request.json['description']
    db.session.commit()
    return {"message": "Drink updated successfully"}