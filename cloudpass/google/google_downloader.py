import re
import requests

from google.constants import START, END
from common.exceptions import ResponseException


def get_download_link(start_link, start=START, end=END):
    file_id_pattern = r'\/(?P<id>[\w\-]+[^\/])\/view'
    link = re.search(file_id_pattern, start_link)
    id = link.group('id')
    return f'{start}id={id}&{end}'


def get_extension(start_link):
    filename_pattern = (r"title':\s(?P<filename>'"
                        r"([\w]+[-]*[\s]*)+\.(?P<ext>[\w]+)')")
    response = requests.get(start_link)
    if response.status_code != 200:
        raise ResponseException()
    content = response.text
    full_filename = re.search(filename_pattern, content)
    extension = full_filename.group('ext')
    return extension


def get_file(start_link):
    download_link = get_download_link(start_link)
    ext = get_extension(start_link)
    response = requests.get(download_link)
    return response.content, ext
