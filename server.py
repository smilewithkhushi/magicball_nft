import flask
from flask import request, jsonify
from flask import render_template as render
import random

app = flask.Flask(__name__,
    template_folder='templates',
    static_folder='static')
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render('index2.html')


@app.route('/question/submit', methods=['POST'])
def q_submit():
    question=request.form['question']
    responses= ['It is certain', "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
    "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentate and ask again", "Don't count on it", "My reply is no", "Outlook not so good", "Very doubtful"]
    respond=random.choice(responses)
    return render("response.html",question=question,response=respond)



@app.route("/mint", methods=['POST'])
def mint():
    question=request.form['question']
    response=request.form['response']
    return render("minted.html",id="")

app.run()