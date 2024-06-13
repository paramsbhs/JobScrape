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