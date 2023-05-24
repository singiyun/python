from selenium import webdriver
from selenium.webdriver.chrome.options import options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)

browser.get("https://nomadcoders.co")