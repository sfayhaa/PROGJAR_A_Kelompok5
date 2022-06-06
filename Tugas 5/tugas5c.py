from platform import java_ver
import requests
import re
from bs4 import BeautifulSoup

header = 'https://pkg.go.dev'

def getGoPackage(query, num):
    address = 'https://pkg.go.dev/search?q=' + query
    print("Requests : {}".format(address))
    r = requests.get(address)

    soup = BeautifulSoup(r.content, 'html.parser')
    link = []

    for i in soup.find('div', {'class':'go-Content'}).find_all('a'):
        text = i.get("href").replace('?tab=licenses', '').replace('?tab=importedby', '').replace('/search-help', '').strip()
        link.append(text)
        
    link_s = sorted(set(link), key=link.index)
    space = ''
    
    n_address = header + link_s[1]
    print("Requests : {}".format(n_address))
    
    r = requests.get(n_address)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    exp = []
    for i in soup.find('section', {'class':'Documentation-index'}).find_all('a'):
        text = i.get_text().replace('¶', '').strip()
        exp.append(text)
       
    print("Results: ")    
    for i in exp:   
        print(i)

if __name__ == '__main__':
    getGoPackage("llrb+petar", 1)
