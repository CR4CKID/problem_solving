from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
import re
from random import choice, randint

pages = set()

# 외부링크가 없을 시 내부링크를 얻는 함수
def getInternalLinks(bs, includeUrl):
    # urlparse: url을 파트별로 나눠주는 함수
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, \
        urlparse(includeUrl).netloc)
    internalLinks = []


    for link in bs.findAll('a', href = re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (str(link.attrs['href']).startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    for link in bs.findAll('a', href = re.compile('^(http|www)((?!' + \
        excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('외부 링크가 존재하지 않음.')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, \
        urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        if len(internalLinks) == 0:
            return 0
        else:
            return getRandomExternalLink(choice(internalLinks))
    else:
        return choice(externalLinks)

def followExternalOnly(startingsite):
    externalLink = getRandomExternalLink(startingsite)
    if externalLink != 0:
        print('무작위 외부 링크 : {}'.format(externalLink))
        followExternalOnly(externalLink)
    else:
        print('사이트 내에 외부링크가 존재하지 않습니다')
followExternalOnly('https://www.oreilly.com')