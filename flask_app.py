from flask import Flask, redirect, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template("resume.html")

@app.route('/contact', methods=['POST','GET'])
def contact():
    return render_template("contact.html")
