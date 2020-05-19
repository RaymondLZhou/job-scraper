import json

with open("data.json") as json_data:
    jobData = json.load(json_data)

for job in jobData:
    print("Title: " + job["title"])
    print("Company: " + job["company"])
    print("Location: " + job["location"])
    print("Link: " + job["link"])
    print()