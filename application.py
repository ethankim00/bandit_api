# using flask_restful
import os
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from get_words import get_new_words
import numpy as np
import json



# Load Words
with open("Data/nodes.json", "r") as file:
    words = json.load(file)
    


app = Flask(__name__)
api = Api(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True



@app.route("/")
def index():
    return render_template("index.html")





class Prediction(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        word = data['word']

        result = get_new_words(word, words)
        # Make prediction using imported model
        return result

api.add_resource(Prediction, '/predict')

if __name__ == '__main__':

    app.run(debug = True)