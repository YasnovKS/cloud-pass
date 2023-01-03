import json
import re

import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

from common.exceptions import ResponseException
from yandex.constants import YANDEX_LINK

load_dotenv()


def get_file(link):

    full_link = f'{YANDEX_LINK}{link}'

    response = requests.get(full_link)
    if response.status_code != 200:
        raise ResponseException()

    soup = bs(response.text, 'lxml')
    p = soup.find('p')
    json_object = json.loads(p.text)
    href = json_object['href']
    # getting file name:
    filename = re.search(r'filename=.*\.\w+', href)
    # getting extension:
    ext = filename.group().split('.')[-1]

    response = requests.get(href)
    return response.content, ext
