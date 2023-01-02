from django.shortcuts import render
from requests import get, post
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import ProjetoDjango


#Create your views here
def homepage(request):
    submitbutton = request.POST.get('submit')

    context = {}
    if request.method == "POST":
        url = request.POST.get('url', None)
        link = cralwer(url)
        s = link.status()
        d = link.detail()
        x = link.subtitle()
        context['link'] = s
        context['detail'] = d
        context['subtitle'] = x
        context['submitbutton'] = submitbutton



    return render(request, 'home.html', context=context
                  )



# Declarando a classe Pai
class cralwer:
    def __init__(self, url):
        self.site = url

    def status(self):
        self.resposta = get(self.site)
        return (self.resposta)

    def detail(self):
        self.tags = BeautifulSoup(self.resposta.text, "html5lib")
        self.title = self.tags.find('title')
        self.subtitle2 = self.tags.find_all("div", {"class": "hatnote"})
        [h2.text for h2 in self.subtitle2]
        self.para_visitar = [self.site + h2.a["href"] for h2 in self.subtitle2]
        return self.para_visitar

    def subtitle(self):
        self.tags = BeautifulSoup(self.resposta.text, "html5lib")
        self.title = self.tags.find('title')
        self.subtitle2 = self.tags.find_all("div", {"class": "hatnote"})

        self.para_visitar = [h2.text for h2 in self.subtitle2]
        return self.para_visitar

    def order_sites(self):
        sites = []
        for pv in self.para_visitar1:
            acesso = get(pv)
            sites.append(acesso.ok)
        for c, v in enumerate(sites):
            print(c, v)


