import flask
from flask import request, jsonify
from flask import render_template as render
import random
import base64
from PIL import Image, ImageDraw
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
import os
from dotenv import load_dotenv
import io

load_dotenv() 
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

NETWORK = "mumbai"

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY,NETWORK)

contract = sdk.get_nft_collection("0xA550040e9b90d8D5afec67b86e44f50356F6FCe6")




app = flask.Flask(__name__,
    template_folder='templates',
    static_folder='static')
app.config["DEBUG"] = True


def create_img(q,r):
    img = Image.new('RGB', (500, 500), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10,10), q, fill=(0,0,0))
    im2 = Image.open('8-Ball.jpg')
    img.paste(im2, (100, 100))
    d.text((10,450), r, fill=(0,0,0))
    img.save('final.jpg', quality=100)

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
    create_img(question,response)
    with open("final.jpg", "rb") as img_file:
        b64_img = base64.b64encode(img_file.read())
    return render("mint.html",base64=b64_img.decode("utf-8"))


@app.route('/mint_nft', methods=['POST'])
def mint_nft():
    address=request.form['address']
    base_64=base64.b64decode(request.form["b64_img"])
    image = Image.open(io.BytesIO(base_64))
    image.save("final.png")
    metadata = NFTMetadataInput.from_json({
        "name": "MagicBall8_NFT",
        "image": open("final.png", "rb"),
    })
    tx = contract.mint_to(address, metadata)
    receipt = tx.receipt
    token_id = tx.id
    with open("final.jpg", "rb") as img_file:
        b64_img = base64.b64encode(img_file.read())
    return render("minted.html",token_id=token_id,base64=b64_img.decode("utf-8"))


app.run()