from bs4 import BeautifulSoup
import sqlite3
import requests

connection = sqlite3.connect("crawled.db")
queue = []
crawled = []
depth = 5

def crawler(url):
    global depth
    depth -= 1
    if(url[0:4] != 'http'):
        url = 'http://' + url
    r = requests.get(url)
    data = r.text
    # print(r.text)

    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all('a'):
        new = str(link.get('href'))
        if new not in queue:
            if(new[0] == '/' and new[1] != '/'):
                new = url[0 : len(url)-1] + new
            if (new[0] == '/' and new[1] == '/'):
                new = "http:" + new
            queue.append(new)
            #print(new)

    print("ONE ITERATION COMPLETED")
    crawled.append(url)

    if(depth > 0):
        crawler(queue.pop(0))


url = input("Enter a website to extract the URL's from: ")
crawler(url)

print("The following sites have been crawled:")
for site in crawled:
    print(site)
    print('\n')
print("TOTAL SITES CRAWLED:" , len(crawled))


print("The following sites are in queue:")
for site in queue:
    print(site)
    print('\n')
print("TOTAL SITES IN QUEUE:" , len(queue))




