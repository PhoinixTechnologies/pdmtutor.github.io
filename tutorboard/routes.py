from flask import Blueprint, request, jsonify  # Import necessary modules
from .models import User, db  # Import User model and database object

# Define a Flask Blueprint for organizing routes
main = Blueprint('main', __name__)

# Define the home route (GET request)
@main.route('/')
def home():
    return jsonify({'message': 'Welcome to the backend!'})  # Return a simple JSON response

# Define a route to handle form submissions (POST request)
@main.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Get the JSON data sent by the client (JavaScript)
    
    # Create a new user instance using the data received
    new_user = User(username=data['username'], password=data['password'])
    
    # Add the new user to the database and commit the transaction
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully!'})  # Return a success response
