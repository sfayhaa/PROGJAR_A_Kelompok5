from platform import java_ver
import requests
import re
from bs4 import BeautifulSoup

header = 'https://pkg.go.dev'

def getGoPackage(query, num):
    if query=="llrb":
        print("Requests : https://pkg.go.dev/search?q=llrb\n")
        if int(num) < 25:
            r = requests.get('https://pkg.go.dev/search?q=llrb')
        else: r= requests.get('https://pkg.go.dev/search?limit=100&m=package&q=llrb#more-results')
     
    if query=="sort":
        print("Requests : https://pkg.go.dev/search?q=sort\n")
        if int(num) < 25:
            r = requests.get('https://pkg.go.dev/search?q=sort')
        else: r = requests.get('https://pkg.go.dev/search?limit=100&m=package&q=sort#more-results')
        
    soup = BeautifulSoup(r.content, 'html.parser')
    link = []
    exp = []

    for i in soup.find('div', {'class':'go-Content'}).find_all('a'):
        text = i.get("href").replace('?tab=licenses', '').replace('?tab=importedby', '').replace('/search-help', '').strip()
        link.append(text)
        
    for i in soup.find('div', {'class':'go-Content'}).find_all('p', attrs={'class':'SearchSnippet-synopsis'}):
        text = i.get_text().strip()
        exp.append(text)
     

    exp_s = sorted(set(exp), key=exp.index)
    exp_n = exp_s[0:int(num)]
    link_s = sorted(set(link), key=link.index)
    link_n = link_s[1:int(num)+1]
    space = ''
    
    count = 1
    for i in range(int(num)):
    	print("{}. {}\nLink: {}{}\n".format(i+1, exp_n[i], header, link_n[i]))


if __name__ == '__main__':
    query = input("Query (llrb or sort): ")
    n = input("Number of Packages: ")

    getGoPackage(query, n)
