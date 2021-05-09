import flask
from flask_cors import CORS
#import back

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#word=back.text
#resp={"response":word.group()}


@app.route('/', methods=['GET'])
def main():
    return "text debug"


@app.route('/hello', methods=['GET'])
def home():
    return "<h1>Hello from Flask</h1>"

app.run(host='projarka-back',port='8887')

