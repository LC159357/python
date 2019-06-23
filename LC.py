import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
res = resquests.get(url)
HTML = res.text
print(HTML)
urls = HTML.split('\n')
    for url in urls:
        name = url.split('/')[-1].strip('\r')
            print(name)
            response = resquest.get(url)
            content = response.content
            with open(name,'wb') as f:
                f.write(content)
            break