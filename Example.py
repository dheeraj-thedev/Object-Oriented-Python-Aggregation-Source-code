
#This will not run on online IDE

import requests
from bs4 import BeautifulSoup
 
URL = "http://localhost:8080/d/2017015447.html"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]  # a list to store quotes
 
table = soup.findAll('div')
 
 
print(table)
