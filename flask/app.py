from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from main import main

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
app.config['UPLOAD_FOLDER'] =  "tmp/"


# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')

# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return main(file_path)

app.run(port = 5000)