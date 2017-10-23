import urllib.request

with urllib.request.urlopen("http://www.hp.com",data=None, timeout=None, cafile=None, capath=None, cadefault=False, context=None) as response:
    html = response.read()
print(html)

contents = html.readlines()
