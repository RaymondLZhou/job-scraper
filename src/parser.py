import json

def jsonPrintEntry(entry):
    print(entry["title"])
    print(entry["company"])
    print(entry["location"])
    print(entry["time"])
    print(entry["link"])
    print(entry["source"])
    print()

def jsonPrintFile(file):
    for entry in file:
        jsonPrintEntry(entry)

def jsonReadFile(path):
    with open(path) as json_data:
        jobData = json.load(json_data)
    
    return jobData

path = "..\\data\\jobs.json"
jobData = jsonReadFile(path)
jsonPrintFile(jobData)