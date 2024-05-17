This repository will include a README file with comprehensive explanations and examples, as well as the necessary code files and directory structure.

### Repository Structure

```
template-inheritance-jinja2/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
├── app.py
├── requirements.txt
├── README.md
```

### 1. `README.md`

```markdown
# Template Inheritance in Jinja2

This repository demonstrates the concept of template inheritance in Jinja2, a templating engine for Python web frameworks like Flask.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Template Files](#template-files)
  - [base.html](#basehtml)
  - [home.html](#homehtml)
  - [about.html](#abouthtml)
- [License](#license)

## Introduction

Jinja2's template inheritance allows you to build a base template that contains common elements for your site (like a header, footer, and navigation) and then create child templates that extend this base template. This helps keep your templates DRY (Don't Repeat Yourself) and makes maintenance easier.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/template-inheritance-jinja2.git
   cd template-inheritance-jinja2
   ```

2. Create a virtual environment and install dependencies:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```sh
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

The application demonstrates template inheritance using three main templates: `base.html`, `home.html`, and `about.html`.

- `base.html`: The base template that includes the common layout.
- `home.html`: The home page template that extends `base.html`.
- `about.html`: The about page template that extends `base.html`.

## Template Files

### base.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 My Website</p>
    </footer>
</body>
</html>
```

### home.html

```html
{% extends 'base.html' %}

{% block title %}Home - My Website{% endblock %}

{% block content %}
    <h2>Home Page</h2>
    <p>Welcome to the home page!</p>
{% endblock %}
```

### about.html

```html
{% extends 'base.html' %}

{% block title %}About - My Website{% endblock %}

{% block content %}
    <h2>About Us</h2>
    <p>This is the about page.</p>
{% endblock %}
```

## License

This project is licensed under the MIT License.
```

### 2. `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. `requirements.txt`

```
Flask==2.1.1
```

### 4. Template Files

- `templates/base.html`
- `templates/home.html`
- `templates/about.html`

These files are already outlined in the `README.md`.

