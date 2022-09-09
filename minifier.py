import requests

reddit_css_max_length = 100 * 1024 # 100 KiB

url = 'https://www.toptal.com/developers/cssminifier/api/raw'
data = {'input': open('stylesheet.css', 'rb').read()}
response = requests.post(url, data=data)

with open('stylesheet.css.mini', 'w') as m:
    length = len(response.text)
    if length > reddit_css_max_length:
        print("WARNING: New stylesheet is too long.")
    used = round(float(length)/reddit_css_max_length, 4)
    print("Used size: %s%% of 100 KiB" % (used * 100))
    m.write(response.text)
