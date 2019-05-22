import urllib.request
response = urllib.request.urlopen('https://www.onliner.by/')
print(response.read())
