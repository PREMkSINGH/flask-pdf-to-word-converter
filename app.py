from flask import Flask,render_template,request
from flask import *
from fileinput import filename
import os
from werkzeug.utils import secure_filename
from pdf2docx import Converter
 

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads'
@app.route('/')
def home():
    for i in os.listdir("uploads"):
        os.remove(r"uploads/"+i)
    return render_template('index.html')

@app.route("/convert",methods=['POST'])
def con():
    full_path=os.path.join(app.config['UPLOAD_FOLDER'])
    fname=request.files['pdf_file']

    fname.save(os.path.join(full_path,fname.filename))
    
    f2conv=os.path.join(full_path,fname.filename)
    fs=fname.filename.split('.')[0]+'.docx'
    docx_file=os.path.join(full_path,fs)
    cv=Converter(f2conv)
    cv.convert(docx_file,start=0,end=None)
    cv.close()

    return send_from_directory(full_path,fs)  


if __name__=='__main__':
    app.run(debug=True)