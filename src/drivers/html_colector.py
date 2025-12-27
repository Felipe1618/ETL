
from typing import List, Dict
from bs4 import BeautifulSoup


class HtmlCollector:

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')

        artist_name_list = soup.find(class_='BodyText')
        artist_name_list_itens = artist_name_list.find_all('a')

        essentials_information = []
        for artist_name in artist_name_list_itens:
            names = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')
            essentials_information.append({
                "name": names,
                "link": links
            })

        return essentials_information