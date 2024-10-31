#Toteuta sovellus tähän tiedostoon
# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import os
app = Flask(__name__)

# @app.route määrää mille osoitteille tämä funktio suoritetaan
@app.route('/')
def hello_world():
    return Response("Hello World!", content_type="text/plain; charset=UTF-8")
    

