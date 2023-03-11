import requests
from bs4 import BeautifulSoup
import re

from settings import start_url, end_url

wiki = 'https://ru.wikipedia.org'


def get_page_valid_links(url: str) -> list:
    """
    returns list of links for a given wiki url
    :param url:
    :return:
    """
    # TODO: check if url is correct
    resp = requests.get(url)
    resp_soup = BeautifulSoup(resp.text, 'html.parser')
    valid_links = [str(i)[8:-4] for i in resp_soup.find_all('a', href=True) if str(i).startswith('<a href="/wiki/')]
    valid_links = [re.findall('"([^"]*)"', i)[0] for i in valid_links]

    return valid_links


def is_target_page(valid_links: list) -> bool:
    """
    Checks if the end_url is on a given page
    :param valid_links: [list of found internal wiki links]
    :return:
    """
    if end_url.replace(wiki, '') in valid_links:
        return True
    return False


def get_path() -> list:
    """
    finds path between two articles
    :return: list[url]
    """
    path = [
        start_url.replace(wiki, ''),
    ]
    first_page = get_page_valid_links(start_url)
    if is_target_page(first_page):
        path.append(end_url.replace(wiki, ''))
        return path

    for link in first_page:
        current = get_page_valid_links(wiki + link)
        if is_target_page(current):
            path.append(link)
            path.append(end_url.replace(wiki, ''))
            return path
    # TODO: add more steps


def main():
    """
    Runs all funcs one by one, prints steps
    :return:
    """

    url_path = get_path()
    output = {}
    try:
        len(url_path)
    except TypeError:
        print('No connections found in 3 steps...')
        return

    for page in range(len(url_path)):
        response = requests.get(wiki + url_path[page])
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            title = soup.find('a', href=url_path[page + 1]).get_text()
        except IndexError:
            break
        for i in soup.find_all('p'):
            if title in str(i):
                # TODO: add ways to collect text from different containers
                output[wiki + url_path[page + 1]] = (i.get_text())
    for num, item in enumerate(output.items()):
        print(f'{num + 1}--------------')
        print(item[1][:-2])  # there is \n at the end of the text, removes it
        print(item[0])
        print()


if __name__ == '__main__':
    if start_url != '' and end_url != '':
        print('looking for connections...')
        main()
    else:
        start_url = str(input('Enter start url: '))
        end_url = str(input('Enter end url: '))
        print('looking for connections...')
        main()
