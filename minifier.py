import requests

url = 'https://cssminifier.com/raw'
data = {'input': open('stylesheet.css', 'rb').read()}
response = requests.post(url, data=data)

with open('stylesheet.css.mini', 'w') as m:
    m.write(response.text)
