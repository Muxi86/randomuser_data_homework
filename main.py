import json

f = open('randomuser_data.json').read()
data = json.loads(f)

results = data['results']

for user in results:
    name = user['name']
    print(name['first'],name['last'])