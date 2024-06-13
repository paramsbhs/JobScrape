import requests
from bs4 import BeautifulSoup

# URL of the job postings page
def get_url():
    return "https://learninginmotion.uvic.ca/myAccount/co-op/postings.htm"

url = get_url()

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


cards = soup.find_all('div', class_='searchResult')


jobs = []
for card in cards:
    atag = card.find('a')
    job_title = atag.get('title')
    job_url = 'https://learninginmotion.uvic.ca' + atag.get('href')
    company = card.find('span', class_='overflowToTitle').text.strip()
    
    jobs.append({
        'job_title': job_title,
        'job_url': job_url,
        'company': company
    })

for job in jobs:
    print(f"Job Title: {job['job_title']}")
    print(f"Company: {job['company']}")
    print(f"Job URL: {job['job_url']}")
    print('-' * 20)