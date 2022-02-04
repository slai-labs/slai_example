from flask import Flask
import slai
import pandas
import os

app = Flask(__name__)

slai.login(
    client_id=os.environ["SLAI_CLIENT_ID"],
    client_secret=os.environ["SLAI_CLIENT_SECRET"]
)

model = slai.model("rissem@gmail.com/california-housing-with-scikit-learn/linear-regression")

data = {"latitude": [40.7, 22.7], "longitude": [-74.0, 23.0], "housing_median_age": [1,2], 
        "total_rooms": [4,5], "total_bedrooms": [3,4], "population": [1,2], "households": [1,2], "median_income": [1,2]}

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/slai")
def slai_proxy():
    df = pandas.DataFrame(data=data)
    predictions = model(x1=df)    
    return f"<p>Hello, World!<br />{predictions}</p>"