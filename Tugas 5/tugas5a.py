import re
import requests
from bs4 import BeautifulSoup

link = 'https://go.dev/doc/'
h_link = 'https://go.dev'
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

def getGoBlog(num):
    
    track_title = num.text.strip().replace(': ', '-')
    download_url = '{}{}'.format(h_link, num['href'])
    file_name = '{}.html'.format(track_title)

    r = requests.get(download_url, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)

    print('Parsing...\n{}: {}'.format(track_title, download_url))

if __name__ == '__main__':
    index = 'a'
    input_link = soup.find_all(index, string=re.compile(r'^((?!\().)*$'))
    count = 1;
    print("List of <{}>\n".format(index))
    for item in input_link[12:21]:
        print(count, item)
        count += 1
    
    print("\nParse which number?")
    num = int(input(">"))

    if num>=count :
        print("Index Out of Range")
    else:
        getGoBlog(input_link[num+11])
        
