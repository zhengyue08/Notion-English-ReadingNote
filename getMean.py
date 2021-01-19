import re
import urllib
from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def mean(word):
    url = 'http://dict.youdao.com/search?q='+(word)
    print(url)
    response = urllib.request.urlopen(url)


    html = response.read().decode('utf-8')
    bs = BeautifulSoup(html, "html.parser")


    pos = bs.select('.pos')
    sen = bs.select('.def')
    print("MeanOK")
    return sen


 