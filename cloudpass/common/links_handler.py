import re

from common.exceptions import WrongLinkException
import google.google_downloader as google
import yandex.yandex_downloader as yandex

POSSIBLE_PREFIXES = {
    'disk.yandex.ru': yandex,
    'drive.google.com': google,
    'yadi.sk': yandex,
}


class Link:
    def __init__(self, raw_link):
        self.link = raw_link

    def get_prefix(self):
        pattern = r'//(?P<prefix>[\w|\.]+)\/'
        match = re.search(pattern, self.link)
        try:
            prefix = match.group('prefix')
        except AttributeError:
            raise WrongLinkException()
        return prefix

    def get_downloader(self):
        prefix = self.get_prefix()
        downloader = POSSIBLE_PREFIXES.get(prefix)
        if not downloader:
            raise WrongLinkException()
        return downloader
