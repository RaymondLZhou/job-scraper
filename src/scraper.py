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

url = "https://www.monster.ca/jobs/search/?q=Software-Intern&tm=30"
job_elems = retriever.retrieveJobs(url)
source = "Monster"
processor.processDataMonster(job_elems, source, jobList, titles, companies, locations, times, links, sources)

jobFrame = builder.frameBuild(titles, companies, locations, times, links, sources)

jsonPath = "..\\data\\jobs.json"
csvPath = "..\\data\\jobs.csv"

writer.dataWrite(jsonPath, jobList, csvPath, jobFrame)
