"""
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code !=200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
"""

def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")

say_hello("singiyun", 24)
say_hello(age=12, name="sinigyun")