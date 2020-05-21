import json

with open("..\\data\\jobs.json") as json_data:
    jobData = json.load(json_data)

for job in jobData:
    print(job["title"])
    print(job["company"])
    print(job["location"])
    print(job["time"])
    print(job["link"])
    print(job["source"])
    print()