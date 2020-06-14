import requests
from bs4 import BeautifulSoup

# Retireves information from Monster based on HTML layout of page
def retrieveJobsMonster(url):
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elems = results.find_all("section", class_="card-content")
    return job_elems

# Retireves information from Indeed based on HTML layout of page
def retrieveJobsIndeed(url):
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("td", id="resultsCol")
    job_elems = results.find_all("div", class_="jobsearch-SerpJobCard")
    return job_elems
    