from urllib.request import urlopen

import requests



r = requests.get("https://xkcd.com/353/")

h = ""
for x in r.iter_lines():
    if ".png" in str(x) and "http" in str(x):
        h = str(x.decode("utf-8")) # change from bytes to string

link_to_image = h[h.find("http"):] # We've found the link to the image.

i = requests.get(link_to_image)

with open("new_image.jpg", "wb") as f: # How to write an image bytes to png.
    f.write(i.content)

print(i.status_code) # How to check code of the site you've accessed
print(i.headers) # How to check https protocol headers.


a = requests.session() # As a context manager
a1 = a.get("http://www.facebook.com")
print(a1.text[0:400])
