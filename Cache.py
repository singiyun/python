#main.py
from flask import Flask, render_template
from extractors.indeed import extract_inddeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")



@app.route("/")
def home():
  return render_template("home.html", name="singiyun")

db= {}

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword in db:
    jobs = db['python']
  else:
    indeed = extract_inddeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
