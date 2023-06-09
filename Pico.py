#home.html
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
  <h1>Job Scrapper</h1>
  <h4>What job do you want?</h4>
  <form action="/search">
    <input type="text" name="keyword" placeholder="Write keyword please" />
    <button>Search</button>
  </form>
</body>
</html>

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
  <h1>Search Results for "{{keyword}}":</h1>
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