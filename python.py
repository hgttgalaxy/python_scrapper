
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
soup = BeautifulSoup(browser.page_source, "html.parser")


print(soup)










'''
input("Press Enter to close the browser")
browser.quit()

'''
from extractors.wwr import extract_wwr_jobs

'''
key = input("입력하세요: ")

jobs = extract_wwr_jobs(key)
print(jobs)


base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f'{base_url}{search_term}')

if response.status_code != 200:
	print("Can't read page")
else:
	print(response.text)

'''
