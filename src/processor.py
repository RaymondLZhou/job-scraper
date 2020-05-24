import linker

def processDataMonster(job_elems, source, jobList, titles, companies, locations, times, links, sources):
    for job_elem in job_elems:
        title_elem = job_elem.find("h2", class_="title")
        company_elem = job_elem.find("div", class_="company")
        location_elem = job_elem.find("div", class_="location")
        time_elem = job_elem.find("div", class_="meta flex-col")

        title, company, location, time = linker.verifyData(title_elem, company_elem, location_elem, time_elem)

        if(title == "" and company == "" and location == "" and time == ""):
            continue
        
        time = time.split('\n')[0]
        link = job_elem.find("a")["href"]

        linker.appendData(title, company, location, time, link, source, jobList, titles, companies, locations, times, links, sources)

def processDataIndeed(job_elems, source, jobList, titles, companies, locations, times, links, sources):
    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('div', class_='location')
        time_elem = job_elem.find("span", class_="date")

        if(location_elem is None):
            location_elem = job_elem.find('span', class_='location')

        title, company, location, time = linker.verifyData(title_elem, company_elem, location_elem, time_elem)

        if(title == "" and company == "" and location == "" and time == ""):
            continue

        if(company == "The Sydney Call Centre"):
            continue
        
        link = "https://ca.indeed.com" + job_elem.find("a")["href"]

        linker.appendData(title, company, location, time, link, source, jobList, titles, companies, locations, times, links, sources)
        