import flask
from flask_cors import CORS
import sql_query

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

word=sql_query.text


@app.route('/', methods=['GET'])
def main():
    return flask.jsonify(response=word)


@app.route('/hello', methods=['GET'])
def home():
    return "<h1>Hello from Flask</h1>"

app.run(host='projarka-back',port='8888')

