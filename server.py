import flask
from flask import request, jsonify
from flask import render_template as render

app = flask.Flask(__name__,
    template_folder='templates',
    static_folder='static')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render('index.html')

app.run()