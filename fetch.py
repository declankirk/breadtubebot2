#This code was written by Boidushya Bhattacharya on Friday, 20 September 2019 at 15:59 p.m.
#Reddit: https://reddit.com/u/Boidushya
#Facebook: https://facebook.com/soumyadipta.despacito
#
#Modified by Declan Kirk for his dumbass bot

from bs4 import BeautifulSoup as bs
import urllib.request
from random import choice as rc
import sys
import os
import requests

def reqImg():
    r = requests.get("https://www.shitpostbot.com/api/randsource")
    img_url = "https://www.shitpostbot.com/"
    content = str(r.content)[2:-1:]
    content = content.replace('null', '0')
    img_url += eval(content)['sub']['img']['full'].replace('\\', '')
    return img_url

def get_lnk(query,sort = 'random'):
    url = "https://www.shitpostbot.com/gallery/sourceimages?review_state=accepted&query=" + query +"&order=total_rating&direction=DESC"
    response = urllib.request.urlopen(url)
    soup = bs(response,'lxml')
    result = []
    for div in soup.findAll('div', attrs={'class':'img'}):
        result.append(div.find('a')['href'])
    if len(result) == 0:
        return ''
    else:
        if sort == 'random':
            fin = rc(result)
        elif sort == 'top':
            fin = result[0]
        return 'https://www.shitpostbot.com' + fin

def get_img(cmd,sort='random'):
    url = get_lnk(cmd,sort)
    if not url:
        return ''
    response = urllib.request.urlopen(url)
    soup = bs(response,'lxml')
    for div in soup.findAll('div', attrs={'style':'padding-top: 15px'}):
        return 'https://www.shitpostbot.com' + (div.find('a')['href'])

def dl(url):
    urllib.request.urlretrieve(url, 'thumb.jpg')
    print('Successfully downloaded ' + url.replace('https://www.shitpostbot.com/img/sourceimages/', ''))

def fetch(args):
    if len(args) == 0:
        print('Downloading random...')
        image = reqImg()
        dl(image)
    else:
        url = ''
        for a in args:
            url = get_img(str(a))
            if url:
                print('Thumbnail found for \'' + a + '\'...')
                break
        if not url:
            print('Nothing found, downloading random...')
            image = reqImg()
            dl(image)
        else:
            dl(url)
