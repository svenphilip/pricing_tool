from flask import Flask, render_template, request, redirect, session, flash

#configure application
app = Flask(__name__)

@app.route("/index", methods=["POST", "GET"])
def index():
    return render_template("index.html")
