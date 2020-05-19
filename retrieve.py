from requests import get
from bs4 import BeautifulSoup

URL = "https://www.monster.ca/jobs/search/?q=Software-intern&where=Toronto&stpage=1&page=2"
page = get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')

    if None in (title_elem, company_elem, location_elem):
        continue

    link = job_elem.find('a')['href']

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(link)
    print()

# filtered_jobs = results.find_all('h2', string=lambda text: 'developer' in text.lower())
# print(len(filtered_jobs))