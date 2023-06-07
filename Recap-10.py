from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html", name="singiyun")


@app.route("/hello")
def hello():
  return render_template("search.html")


app.run("0.0.0.0")
