import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def retrieveJobs(url):
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elems = results.find_all("section", class_="card-content")
    return job_elems

url = "https://www.monster.ca/jobs/search/?q=Software-intern&where=Toronto&stpage=1&page=2"

job_elems = retrieveJobs(url)
source = "Monster"

jobList = []
titles = []
companies = []
locations = []
times = []
links = []
sources = []

def appendData(title, company, location, time, link, source, jobList, titles, companies, locations, times, links, sources):
    jobObject = {
        "title": title,
        "company": company,
        "location": location,
        "time": time,
        "link": link,
        "source": source
    }

    jobList.append(jobObject)
    titles.append(title)
    companies.append(company)
    locations.append(location)
    times.append(time)
    links.append(link)
    sources.append(source)

def processData(job_elems, source, jobList, titles, companies, locations, times, links, sources):
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

        appendData(title, company, location, time, link, source, jobList, titles, companies, locations, times, links, sources)

processData(job_elems, source, jobList, titles, companies, locations, times, links, sources)

def frameBuild(titles, companies, locations, times, links, sources):
    jobFrame = pd.DataFrame({
        "title": titles,
        "company": companies,
        "location": locations,
        "time": times,
        "link": links,
        "source": sources
    })

    return jobFrame

jobFrame = frameBuild(titles, companies, locations, times, links, sources)

def jsonWrite(path, jsonList):
    with open(path, "w") as outfile:
        json.dump(jsonList, outfile, ensure_ascii=False, indent=4)

def csvWrite(path, csvFrame):
    csvFrame.to_csv("..\\data\\jobs.csv")

def dataWrite(jsonPath, jsonList, csvPath, csvFrame):
    jsonWrite(jsonPath, jsonList)
    csvWrite(csvPath, csvFrame)

jsonPath = "..\\data\\jobs.json"
csvPath = "..\\data\\jobs.csv"

dataWrite(jsonPath, jobList, csvPath, jobFrame)
