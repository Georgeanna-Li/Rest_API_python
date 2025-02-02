# This is a REST API project

This project is a simple REST API for managing a list of drinks. The API is built using Flask and SQLAlchemy.

## Features

- **View all drinks**: `GET /drinks`
- **View a specific drink**: `GET /drinks/<id>`
- **Add a new drink**: `POST /drinks`
- **Delete a drink**: `DELETE /drinks/<id>`

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- Flask
- Flask-SQLAlchemy

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/drinks-api.git
   cd drinks-api

2. **Create and activate a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

    ```sh
    pip install Flask Flask-SQLAlchemy

4. **Run the application:**

    ```sh
    export FLASK_APP=application.py
    export FLASK_DEBUG=1  # For development mode
    flask run

    
A little bit instruction about these three lines:

1. Setting the Flask Application Entry Point:

`export FLASK_APP=application.py`

This line sets the FLASK_APP environment variable to application.py. This tells Flask which file to look for when starting the application. When you run flask run, Flask uses the value of FLASK_APP to find the application instance.

2. Setting the Flask Environment:

`export FLASK_DEBUG=1`

Instead of setting FLASK_ENV=development, you can use FLASK_DEBUG=1 to enable debug mode. This mode provides helpful error messages and an interactive debugger in the browser when something goes wrong with your application.

Debug mode also enables auto-reload, which means the server will automatically reload and apply changes whenever you modify your code, making development faster and easier.

3. Run Flask.

`flask run`

Usage
You can test the API using tools like curl, httpie, or Postman.


## Inherit from db.Model

In SQLAlchemy (and Flask-SQLAlchemy), the db.Model class is a base class for all models. When you inherit from db.Model, your class gains a lot of functionality automatically, including the ability to map class attributes to database columns.

There you will notice you don't have any explicit __init__ method because the db.Model base class provides an initializer that automatically handles the initialization of attributes for you. This is a feature of SQLAlchemy's declarative base. When you define class attributes as db.Column, SQLAlchemy's declarative system creates an __init__ method for you.

Here’s an example of what this autogenerated __init__ method might look like:

`
def __init__(self, id=None, name=None, description=None):
    self.id = id
    self.name = name
    self.description = description
`
## More readings

Here we are calling Flask, but you can also implement this in FastAPI. And in this article they talked about how to generate separate files for clairty. 
[How you can modularize your files in FastAPI](https://towardsdev.com/fastapi-from-app-py-to-a-modular-architecture-54ca9e0044eb)
