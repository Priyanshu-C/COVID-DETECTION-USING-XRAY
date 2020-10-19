from flask import render_template,request,Blueprint,redirect
from keras.models import load_model
from cv2 import cv2
import numpy as np
import os
core = Blueprint('core',__name__)

@core.route('/')
def index():       
    return render_template('index.html')                     

@core.route('/', methods = ["POST"])
def ModelTest():
    MODEL = load_model("VGGModel")
    if request.method == "POST":

        data = request.files['imagefile']
        data.save("img")

        image = cv2.imread('img')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = image/255.0
        image = cv2.resize(image, (512, 512))
        image = image.reshape(-1, 512, 512, 3)

        TAG = ["COVID","NORMAL"]
        X = MODEL.predict(image)
        if TAG[np.argmax(X)] == "COVID":
            return render_template('covid.html')
        else:
            return render_template('normal.html')
    

