from requests import get, post
from tinydb import TinyDB
from bs4 import BeautifulSoup
import  html5lib

site = TinyDB('site.json')

def cralwer(self):
    respota = get(self)
    r = respota.ok
    if r == True:
        resp = 'Site validated' \
               ''
    else:
        resp = 'Site not found'
    l = respota.text
    tags = BeautifulSoup(l, "html5lib")
    title = tags.find('title')
    title = title.text
    subtitle2 = tags.find_all("div", {"class": "hatnote"})
    para_visitar = [self + h2.a["href"]  for h2 in subtitle2  ]

    site.insert({'Status': resp,'title':title, 'other_site':[para_visitar]})




