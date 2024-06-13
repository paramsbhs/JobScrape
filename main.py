import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_url(position):
    template = "https://learninginmotion.uvic.ca/myAccount/co-op/postings.htm"
    url = template.format(position)
    return url

url = get_url('software')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('div', 'searchResult')

card = cards[0]
atag = card.h2.a
job_title = atag.get('title')

job_url = 'https://learninginmotion.uvic.ca' + atag.get('href')

company = card.find('span', {"class": "overflowToTitle"}).text.strip()