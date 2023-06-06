from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html", name="singiyun")


@app.route("/hello")
def hello():
  return 'hello you!'

app.run("0.0.0.0")

#home.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Job Scrapper</title>
</head>
<body>
  <h1>Hello to you! My name is {{name}}</h1>
</body>
</html>