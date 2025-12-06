import requests
from bs4 import BeautifulSoup
import re
url = "https://www.jacktuttle.com/product/guitarcollection/?attribute_pa_format=both"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
import os 

def normalize_filename(text):
    return text.replace(' ', '_').replace('/', '_').strip()

mp3_urls = []
def main():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        href = link['href']
        if re.search(r'\.(mp3|m4a)$', href):
            rq = requests.get(href, headers=headers)
            try:
                with open(os.path.abspath(f"./tracks/{normalize_filename(link.text)}.{href.split('.')[-1]}"), "wb") as file:
                    file.write(rq.content)
                    print(f"wrote {normalize_filename(link.text)}.{href.split('.')[-1]} to disk")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()