from requests import get

websites = (
"google.com",
"httpstat.us/100",
"httpstat.us/200",
"httpstat.us/300",
"httpstat.us/400",
"httpstat.us/500"
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
response = get(website)

if response.status_code >= 500:
  results[website] = "server err response"
elif response.status_code >= 400:
  results[website] = "client err response"
elif response.status_code >= 300:
  results[website] = "redirection msg"
elif response.status_code >= 200:
  results[website] = "success response"
elif response.status_code >= 100:
  results[website] = "Info response"

print(results)