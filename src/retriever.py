import requests
from bs4 import BeautifulSoup

def retrieveJobs(url):
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elems = results.find_all("section", class_="card-content")
    return job_elems