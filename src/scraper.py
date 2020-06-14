import numpy as np
import pandas as pd
from time import sleep
from random import randint

# Import modules
import retriever
import processor
import builder
import writer

# Create lists of data to store
jobList = []
titles = []
companies = []
locations = []
times = []
links = []
sources = []

# Retrieve information from Monster
url = "https://www.monster.ca/jobs/search/?q=Software-Intern&tm=30&stpage=1&page=5"
job_elems = retriever.retrieveJobsMonster(url)
source = "Monster"
processor.processDataMonster(job_elems, source, jobList, titles, companies, locations, times, links, sources)

# Retrieve information from Indeed
urlBase = "https://ca.indeed.com/jobs?q=Software+Intern&limit=50&radius=25&start="
pages = np.arange(0, 200, 50)

# Scroll through first 5 pages
for page in pages:
    url = urlBase + str(page)
    job_elems = retriever.retrieveJobsIndeed(url)
    source = "Indeed"

    processor.processDataIndeed(job_elems, source, jobList, titles, companies, locations, times, links, sources)

    sleep(randint(2, 5))

# Create pandas DataFrame
jobFrame = builder.frameBuild(titles, companies, locations, times, links, sources)

jsonPath = "..\\data\\jobs.json"
csvPath = "..\\data\\jobs.csv"

# Write to json and csv files
writer.dataWrite(jsonPath, jobList, csvPath, jobFrame)
