import flask
from flask import request, jsonify
from flask import render_template as render
import requests
import random

app = flask.Flask(__name__,
    template_folder='templates',
    static_folder='static')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render('index.html')


def q_return(q,r):
    return render("response.html",q=q,r=r)

@app.route('/question/submit', methods=['POST'])
def q_submit():
    question=requests.form['question']
    responses=['Yes','No']
    respond=random.choice(responses)
    q_return(question,respond)




app.run()