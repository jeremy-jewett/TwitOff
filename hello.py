from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/new_page')
def new_page():
    return 'This is another page!'


if __name__ == '__main__':
    app.run(debug=True)
# The way I got this to work in the Pycharm environment/terminal:
# set FLASK_APP=hello.py
# flask run
