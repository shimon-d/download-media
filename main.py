import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
domain = 'www.example.com'
url = f'https://{domain}/page5.html'

# Make a GET request to the URL
response = requests.get(url=url, headers=headers)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the audio links on the page
audio_links = soup.find_all('a', href=True)

# Loop through each audio link and download the file
for link in audio_links:
    href = link.get('href')
    if href.endswith('.mp3'):
        url_parts = urllib.parse.urlsplit(href)
        url = urllib.parse.urlunsplit(('https', domain, url_parts.path, url_parts.query, ''))
        response = requests.get(url, headers=headers)
        size = int(response.headers.get('Content-Length', 0))
        with open('downloads/' + href.split('/')[-1], 'wb') as f:
            f.write(response.content)
        print(f'{href} downloaded successfully')
