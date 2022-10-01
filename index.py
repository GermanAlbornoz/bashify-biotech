from flask import Flask, render_template, request, redirect, url_for    
import os
template_dir = os.path.abspath('templates') 
app = Flask(__name__, template_folder=template_dir, static_folder= 'static')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        message = request.form['Message']
    return render_template("index.html")
"""
@app.route("/Cursos")
def cursos():
    return render_template("courses.html")
"""
if __name__== "__main__":
    app.run(debug=True)