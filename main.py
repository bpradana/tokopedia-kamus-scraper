import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
from tqdm import tqdm
import time


def get_urls():
    base_url = 'https://kamus.tokopedia.com/'
    entry_links = []

    print('Getting URLs')
    start = time.time()
    for c in tqdm(ascii_lowercase):
        url = base_url + c

        page = requests.get(url)
        entries = BeautifulSoup(page.content, 'html.parser').find(class_='keyword__list--wrapper').find_all('a')
        
        for entry in entries:
            entry_links.append(entry['href'])
    print('Finished in %d seconds' % (time.time() - start))
    return entry_links


if __name__ == '__main__':
    entry_links = get_urls()