from .... import db  # Import the SQLAlchemy database object from the __init__.py file

# Define a User model representing the 'users' table in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key column (unique ID)
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username field
    password = db.Column(db.String(128), nullable=False)  # Password field (hashed for security)
