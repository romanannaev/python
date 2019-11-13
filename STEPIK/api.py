import requests

with open('dataset_24476_3.txt', 'r') as f:
    numbers = f.readlines()

for number in numbers:
    url = 'http://numbersapi.com/' + number.strip() + '/math?json=true'
    r = requests.get(url)
    resp = r.json()
    if resp['found']:
        print('Interesting')
    else:
        print('Boring')

# import requests
# with open("input.txt") as f:
#     for i in f:
#         api_url = "http://numbersapi.com/{}/math".format(int(i))
#         params = {"json" : True }
#         res = requests.get(api_url,params)
#         data = res.json()
#         if data["found"]:
#             print("Interesting")
#         else:
#             print("Boring")

Не используйте ни format ни +

with open("dataset_24476_3.txt") as f:
    for num in f.read().splitlines():
        api_url = f'http://numbersapi.com/{num}/math'
        params = {'json': 'true'}
        resp = requests.get(api_url, params=params)
        if resp.status_code == 200:
            print("Interesting" if resp.json()['found'] else "Boring")