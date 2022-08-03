import urllib
import urllib.request

try:
    site= urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site {site} não está acessivel no momento')
else:
    print(f'O site {site} está acessivel no momento')
    #print(site.read()) traz o codigo do site


