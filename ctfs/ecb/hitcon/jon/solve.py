from bs4 import BeautifulSoup
import requests
url = 'http://13.115.255.46/'
r = requests.get(url)

data = r.text

soup = BeautifulSoup(data,features="html.parser")
links = soup.find_all('a')[1:]
crypto_data = []
for link in links:
    #print(link.get('href'))
    href = str(link.get('href'))
    title = str(link)[len(link.get('href'))+11:-4]
    h_url = requests.get(url+href).url.encode('utf-8')
    crypto_data.append({'ref':href,'url':h_url})
    print(href,h_url)