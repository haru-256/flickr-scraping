from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報
key = "364b30478726a5efddc13952453a5b0b"
secret = "c178f5e3f3c40be9"
wait_time = 1 #1秒おきにリクエスト
imgname = sys.argv[1]
savedir = "./" + imgname
os.mkdir(savedir)
cnt=0

flickr = FlickrAPI(key, secret, format='parsed-json')
k=0
while True:
    k+=1
    result = flickr.photos.search(
        text = imgname,
        per_page = 10,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        extras = 'url_c, licence',
        page=k
    )
    photos = result['photos']
    for i, photo in enumerate(photos['photo']):
        try:
            url_q = photo['url_c']
        except KeyError:
            continue
        filepath = savedir + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath): continue
        urlretrieve(url_q,filepath)
        cnt+=1
    if cnt > 100:
        break
    print(cnt)

