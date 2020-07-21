# using flask_restful
import os
from flask import Flask, jsonify, request, render_template, session, redirect
from flask_restful import Resource, Api, reqparse
from get_words import get_new_words
import numpy as np
import json



# Load Words
with open("Data/nodes.json", "r") as file:
    words = json.load(file)
    


app = Flask(__name__)
api = Api(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'dfakflsfjs'



@app.route("/")
def index():
    return render_template("index.html", data= session['data'])



class Prediction(Resource):
    @staticmethod
    def post():
        word = request.form.get('word')
        # Make prediction using imported model
        result = get_new_words(word, words)
        session['data'] = result
        return redirect("/")

api.add_resource(Prediction, '/predict')

if __name__ == '__main__':

    app.run(debug = True)