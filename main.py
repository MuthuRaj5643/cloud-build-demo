
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello!'

@app.route('/hi')
def hi():
    return 'Hi'

@app.route('/hello')
def greet():
    return 'Good morning'

@app.route('/muthu')
def muthu():
    return "Hello from Muthu"

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
