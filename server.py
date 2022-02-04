from flask import Flask
import slai
import pandas
import os
import json
from flask import request

app = Flask(__name__)

slai.login(
    client_id=os.environ["SLAI_CLIENT_ID"],
    client_secret=os.environ["SLAI_CLIENT_SECRET"]
)

# TODO Add your SLAI URL here. You can find it in your 
SLAI_URL = "FILL_ME_IN"
model = slai.model(f"{SLAI_URL}/initial")

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

@app.route("/slai", methods = ["POST"])
def slai_proxy():
    data = {key: [request.json[key]] for key in request.json}
    df = pandas.DataFrame(data=data)
    predictions = model(x1=df)["pred"]
    return json.dumps(predictions.tolist())

# For developer sanity. So changes to calculator.js do not require a hard refresh
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r