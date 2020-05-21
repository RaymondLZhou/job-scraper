import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np

url = "https://www.monster.ca/jobs/search/?q=Software-intern&where=Toronto&stpage=1&page=2"
page = requests.get(url, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elems = results.find_all("section", class_="card-content")

# filtered_jobs = results.find_all('h2', string=lambda text: 'developer' in text.lower())

jobList = []

titles = []
companies = []
locations = []
times = []
links = []

for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    time_elem = job_elem.find("div", class_="meta flex-col")

    if None in(title_elem, company_elem, location_elem, time_elem):
        continue

    title = title_elem.text.strip()
    company = company_elem.text.strip()
    location = location_elem.text.strip()
    time = time_elem.text.strip().split('\n')[0] 
    link = job_elem.find("a")["href"]

    jobObject = {
        "title": title,
        "company": company,
        "location": location,
        "time": time,
        "link": link
    }

    jobList.append(jobObject)

    titles.append(title)
    companies.append(company)
    locations.append(location)
    times.append(time)
    links.append(link)

jobFrame = pd.DataFrame({
    "title": titles,
    "company": companies,
    "location": locations,
    "time": times,
    "link": links,
})

with open("data.json", "w") as outfile:
    json.dump(jobList, outfile, ensure_ascii=False, indent=4)

jobFrame.to_csv("data.csv")
