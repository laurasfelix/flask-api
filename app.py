from flask import Flask, render_template, request
import requests
import project
#SWIRCWIP8Z0W6BV

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = project.build()
    return render_template("index.html",data=data)

if __name__ == "__main__":
    app.run()