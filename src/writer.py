import json

def jsonWrite(path, jsonList):
    with open(path, "w") as outfile:
        json.dump(jsonList, outfile, ensure_ascii=False, indent=4)

def csvWrite(path, csvFrame):
    csvFrame.to_csv(path)

def dataWrite(jsonPath, jsonList, csvPath, csvFrame):
    jsonWrite(jsonPath, jsonList)
    csvWrite(csvPath, csvFrame)
    