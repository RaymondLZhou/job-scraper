import pandas as pd

def frameBuild(titles, companies, locations, times, links, sources):
    jobFrame = pd.DataFrame({
        "title": titles,
        "company": companies,
        "location": locations,
        "time": times,
        "link": links,
        "source": sources
    })

    jobFrame["time"] = jobFrame["time"].str.extract('(\\d+)')
    jobFrame["time"] = pd.to_numeric(jobFrame["time"], errors="coerce")

    return jobFrame
    