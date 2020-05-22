def verifyData(title_elem, company_elem, location_elem, time_elem):
    if(title_elem is None):
        title = ""
    else:
        title = title_elem.text.strip()
        
    if(company_elem is None):
        company = ""
    else:
        company = company_elem.text.strip()

    if(location_elem is None):
        location = ""
    else:
        location = location_elem.text.strip()

    if(time_elem is None):
        time = ""
    else:
        time = time_elem.text.strip()

    return title, company, location, time

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