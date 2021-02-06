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
    
    if request.method == "POST":
        selectmodel = request.form.get("selectmodel")
        if selectmodel=="VGG19":
            MODEL = load_model("VGGModel")
            imgsize = 512
        elif selectmodel=="VGG16":
            MODEL = load_model("model_vgg16.h5")
            imgsize = 224

        data = request.files['imagefile']
        data.save("img")

        image = cv2.imread('img')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = image/255.0
        image = cv2.resize(image, (imgsize, imgsize))
        image = image.reshape(-1, imgsize, imgsize, 3)

        TAG = ["COVID","NORMAL"]
        X = MODEL.predict(image)
        X = np.argmax(X)
        return render_template('covid_normal.html',X = X,selectmodel=selectmodel)
    

