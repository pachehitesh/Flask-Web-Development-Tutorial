### Flask SQLAlchemy Tutorial

Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, which is a SQL toolkit and Object-Relational Mapping (ORM) system for Python. This tutorial will guide you through the steps to set up and use Flask-SQLAlchemy in your Flask applications.

#### 1. **Installation**
First, you need to install Flask and Flask-SQLAlchemy. You can do this using pip:

```bash
pip install Flask
pip install Flask-SQLAlchemy
```

#### 2. **Setting Up the Application**
Create a new Flask application and configure it to use SQLAlchemy. Here is a basic example:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, the `SQLALCHEMY_DATABASE_URI` configuration sets up the database. Here, SQLite is used for simplicity, but you can replace it with any other database URI, like PostgreSQL or MySQL.

#### 3. **Creating Models**
Models represent the structure of your database tables. Each model is a Python class that inherits from `db.Model`. Here is an example of a simple `User` model:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

#### 4. **Creating the Database**
To create the database and tables from the models, you need to run the following commands in a Python shell:

```python
from yourapplication import db
db.create_all()
```

This will create the necessary tables in your database.

#### 5. **Adding and Querying Data**
To add data to your database, you need to create an instance of your model and add it to the session:

```python
from yourapplication import db, User

user = User(username='JohnDoe', email='john@example.com', password='password')
db.session.add(user)
db.session.commit()
```

To query data from the database, you can use SQLAlchemy's query interface:

```python
users = User.query.all()
user = User.query.filter_by(username='JohnDoe').first()
```

#### 6. **Updating and Deleting Data**
To update a record, modify its attributes and commit the session:

```python
user = User.query.get(1)
user.email = 'newemail@example.com'
db.session.commit()
```

To delete a record, use the `delete` method and commit the session:

```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

#### 7. **Handling Migrations**
Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. Install it using pip:

```bash
pip install Flask-Migrate
```

Then, set it up in your application:

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

Create a migration repository and generate your initial migration script:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

#### Conclusion
This tutorial covered the basics of setting up Flask-SQLAlchemy, creating models, and performing basic database operations. Flask-SQLAlchemy provides a powerful way to interact with databases in your Flask applications, and with the addition of Flask-Migrate, managing database changes becomes straightforward. For more advanced usage and detailed configurations, refer to the official Flask-SQLAlchemy documentation.
