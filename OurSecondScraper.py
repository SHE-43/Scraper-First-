import requests

payload = {'page':2, 'count':'25'};

link1 = requests.get("https://httpbin.org/get" , params=payload)

print(link1.text)
print(link1.url) # it will show you the link it has requested.
# args = url parameters

payload = {'username':'Hamza','password':'testing'}

link_post = requests.post("https://httpbin.org/post" , data=payload) # this is data for form.

r_dict = link_post.json()

print(r_dict['form']) # Now we can access them separately.

# Basic authentication is when a small screen pops out from above to ask for username and password.
print("\n")
link_auth = requests.get("https://httpbin.org/basic-auth/hamza/malik", auth = ('hamza', 'malik'))

print(link_auth.status_code)
print("\n")

link_delay = requests.get("https://httpbin.org/delay/10", timeout=20)
print(link_delay.status_code) # this shows timeout | this will get an exception
link_delay2 = requests.get("https://httpbin.org/delay/1", timeout=3)
print(link_delay2.status_code)








