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

def processDataMonster(job_elems, source, jobList, titles, companies, locations, times, links, sources):
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