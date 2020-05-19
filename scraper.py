import requests
from bs4 import BeautifulSoup
import json

url = "https://www.monster.ca/jobs/search/?q=Software-intern&where=Toronto&stpage=1&page=2"
page = requests.get(url, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elems = results.find_all("section", class_="card-content")

# filtered_jobs = results.find_all('h2', string=lambda text: 'developer' in text.lower())

jobList = []

for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")

    if None in(title_elem, company_elem, location_elem):
        continue

    link = job_elem.find("a")["href"]

    jobObject = {
        "title": title_elem.text.strip(),
        "company": company_elem.text.strip(),
        "location": location_elem.text.strip(),
        "link": link
    }

    jobList.append(jobObject)

with open("data.json", "w") as outfile:
    json.dump(jobList, outfile, ensure_ascii=False, indent=4)
