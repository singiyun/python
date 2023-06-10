#main.py
from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_inddeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html", name="singiyun")


db= {}


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db['python']
  else:
    indeed = extract_inddeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")

#search.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Job Scrapper</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
</head>
<body>
  <main class="container">
    <hgroup>
        <h1>Search Results for "{{keyword}}":</h1>
    <a target="_blank" href="/export?keyword={{keyword}}">Export to file</a>
    </hgroup>
    <table><figure>
      <thead>
        <tr>
          <th>Position</th>
          <th>Company</th>
          <th>Location</th>
          <th>Link</th>
        </tr>
      </thead>
      <tbody>
      {% for job in jobs %}
      <tr>
        <td>{{job.position}}</td>
        <td>{{job.company}}</td>
        <td>{{job.location}}</td>
        <td></td><a href="{{job.link}}" target="_blank">Apply now&rarr;</a>
      </tr>
    {% endfor %}
      </tbody>
    </table></figure>
  </main>
</body>
</html>