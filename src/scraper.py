import numpy as np
import pandas as pd
from time import sleep
from random import randint

import retriever
import processor
import builder
import writer

jobList = []
titles = []
companies = []
locations = []
times = []
links = []
sources = []

# Monster
url = "https://www.monster.ca/jobs/search/?q=Software-Intern&tm=30&stpage=1&page=5"
job_elems = retriever.retrieveJobsMonster(url)
source = "Monster"
processor.processDataMonster(job_elems, source, jobList, titles, companies, locations, times, links, sources)

# Indeed
urlBase = "https://ca.indeed.com/jobs?q=Software+Intern&limit=50&radius=25&start="
pages = np.arange(0, 200, 50)

for page in pages:
    url = urlBase + str(page)
    job_elems = retriever.retrieveJobsIndeed(url)
    source = "Indeed"

    processor.processDataIndeed(job_elems, source, jobList, titles, companies, locations, times, links, sources)

    sleep(randint(2, 5))

jobFrame = builder.frameBuild(titles, companies, locations, times, links, sources)

jsonPath = "..\\data\\jobs.json"
csvPath = "..\\data\\jobs.csv"

writer.dataWrite(jsonPath, jobList, csvPath, jobFrame)
