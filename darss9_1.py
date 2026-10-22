import json

with open ("Users.json") as f:
    data = json.load(f)
    for royhat in data:
        jami = sum(int(royhat['narxi']))
        print(jami)