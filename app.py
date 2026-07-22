from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pandas as pd
import requests
import pickle
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras_preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import sqlite3

# Define a flask app
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')        
# @app.route('/index', methods=['GET'])
# def index():
#     # Main page
#     return render_template('index.html')

####Plant Leaf Disease Detection with Remedies####

#model_path2 = 'models/model_xception.h5' # load .h5 Model

@app.route('/index')
def index_page():
    return render_template('index.html')  # Create this template



model_path2 = "C:/Users/sindhu gadhe/Documents/diseasse with solution/diseasse with solution/models/model_xception.h5"
classes2 = {0:"Bacteria",1:"Fungi",2:"Nematodes",3:"Normal",4:"Virus"}
CTS = load_model(model_path2)
from keras_preprocessing.image import load_img, img_to_array
def model_predict2(image_path,model):
    print("Predicted")
    image = load_img(image_path,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    
    result = np.argmax(model.predict(image))
    print(result)
    #prediction = classes2[result]  
    
    if result == 0:
        return "Bacteria", "result.html"        
    elif result == 1:
        return "Fungi","result.html"
    elif result == 2:
        return "Nematodes","result.html"
    elif result == 3:
        return "Normal","result.html"
    elif result == 4:
        return "Virus","result.html"
    
    
# login page development
@app.route('/')
def home():
    return render_template('login.html')

@app.route("/signup")
def signup():
    name = request.args.get('username','')
    # contactno = request.args.get('CN','')
    email = request.args.get('email','')
    password = request.args.get('psw','')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "signup.db")
    con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\signup.db')
    cur = con.cursor()
    cur.execute("insert into accounts (name, email, password) VALUES ( ?, ?, ?)",(name,email,password))
    con.commit()
    con.close()

    return render_template("login.html")

@app.route("/signin", methods=['POST'])
def signin():
    mail1 = request.args.get('uname','')
    password1 = request.args.get('psw','')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "signup.db")
    con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\signup.db')
    cur = con.cursor()
    cur.execute("select email, password from accounts where email = ? AND password = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("login.html", error="Invalid credentials")

    elif mail1 == data[0] and password1 == data[1]:
        return render_template("index.html")

    
    else:
        return render_template("login.html", error="Invalid credentials")


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")
# login page completed


@app.route('/logout')
def logout():
    # You can clear session info here if needed
    return redirect(url_for('login'))


@app.route('/predict2',methods=['GET','POST'])
def predict2():
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['file'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        #filename1 = os.path.join(UPLOAD_FOLDER, filename)

        print("@@ Predicting class......")
        pred, output_page = model_predict2(file_path,CTS)

        remdies = 'Normal Leaf' if pred == 'Normal' else 'No remedy found'

        if pred == 'Bacteria':
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            con = sqlite3.connect(os.path.join(BASE_DIR, "remedies.db"))
            con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\remedies.db')
            cur = con.cursor()
            cur.execute("select label from data2 where message = ?",(pred,))
            remdies = cur.fetchall()
        
        elif pred == 'Fungi':
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            con = sqlite3.connect(os.path.join(BASE_DIR, "remedies.db"))
            con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\remedies.db')
            cur = con.cursor()
            cur.execute("select label from data2 where message = ?",(pred,))
            remdies = cur.fetchall()

        elif pred == 'Nematodes':
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            con = sqlite3.connect(os.path.join(BASE_DIR, "remedies.db"))
            con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\remedies.db')
            cur = con.cursor()
            cur.execute("select label from data2 where message = ?",(pred,))
            remdies = cur.fetchall()

        elif pred == 'Virus':
            val = 'viruses'
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            con = sqlite3.connect(os.path.join(BASE_DIR, "remedies.db"))
            con = sqlite3.connect(r'C:\Users\sindhu gadhe\Documents\diseasse with solution\diseasse with solution\remedies.db')
            cur = con.cursor()
            cur.execute("select label from data2 where message = ?",(val,))
            remdies = cur.fetchall()

        else:
            pred = 'Normal'
            remdies = 'Normal Leaf'
              
        return render_template(output_page, pred_output = pred,remdy = remdies, img_src=UPLOAD_FOLDER + file.filename)
    


if __name__== '__main__':
        app.run(debug=True)