import os

from celery import Celery
from .airtable import push
from datetime import timedelta
import random

import requests
from bs4 import BeautifulSoup

app = Celery('tasks',)

app.conf.broker_url = os.environ.get('CLOUDAMQP_URL')
app.conf.beat_schedule = {
    'add-quotes-every-60-seconds': {
        'task': 'tasks.parse_and_publish',
        'schedule': timedelta(seconds=60),
    },
}

url = 'https://quotes.toscrape.com/page/'

@app.task
def parse_and_publish():
    response = requests.get(url + str(random.randint(1,10)))
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    push(quotes=quotes[random.randint(1,10)].text)
