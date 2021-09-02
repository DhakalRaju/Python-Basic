import requests
from bs4 import BeautifulSoup

r = requests.get('https://broadwayinfosys.com/career')

soup = BeautifulSoup(r.content, 'html.parser')

jobs = soup.select('.block-card')

print(jobs[0].find('h3').text)

with open('jobs.txt', 'w') as f:
    for job in jobs:
        f.write(job.find('h3'.text))
        f.write('  ')
        f.write(job.find('h3').get('href'))
        f.write('\n')
        f.write('*' * 15)
        f.write('\n')