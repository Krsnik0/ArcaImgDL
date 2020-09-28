from bs4 import BeautifulSoup
import requests
import os
import urllib.request

sampleUrl = 'https://arca.live/b/lastorigin/8236343'
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


def imgDown(url):
    try:
        savePath = './' + '_'.join((sampleUrl.split('?')[0]).split('/')[-2:])
    except:
        savePath = './Downloads'

    try:
        if not(os.path.isdir(savePath)):
            os.makedirs(os.path.join(savePath))
    except:
        print("Failed to create directory!!!!!")
        return
        
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')
    content = bs.select_one('div.article-content')
    imgs = [x['src'] for x in content.find_all('img')]
    # print(imgs)
    for i, img in enumerate(imgs):
        urllib.request.urlretrieve('https:'+ img, savePath + '/' +  str(i) + '.' + img.split('.')[-1])
    print('saveing Done')

imgDown(input())