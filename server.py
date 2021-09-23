from flask import Flask
from flask_restful import Api, Resource # Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.

app = Flask(__name__)


# The route is used to bind a function to a URL
# The route maps a url to some logic (also known as "view function")
@app.route("/")
# A single function can be associated with multiple routes
# @app.route("/home")
# @app.route("/index")
def home():
    return "Hello World!"


def about():
    return "This is the About Us page..."

# This is another way to add a route
app.add_url_rule(rule="/about", endpoint='about', view_func=about, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)  # setting debug=True will auto-reload the server when a file is changed
