import json
import re
import os

import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from cloudpass.settings import BASE_DIR

load_dotenv()

DIRECTORY = BASE_DIR / 'downloads'


def get_file(link):
    DIRECTORY.mkdir(exist_ok=True)

    api = os.getenv('YANDEX_API')

    full_link = f'{api}{link}'

    response = requests.get(full_link)

    soup = bs(response.text, 'lxml')
    p = soup.find('p')
    json_object = json.loads(p.text)
    anc = json_object['href']
    # getting file name:
    filename = re.search(r'filename=.*\.\w+', anc)
    # getting extension:
    ext = filename.group().split('.')[-1]

    response = requests.get(anc)
    return response.content, ext
