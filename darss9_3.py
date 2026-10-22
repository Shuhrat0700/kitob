import json

with open ("Users1.json") as f:
    data = json.load(f)
    for oraliq in data:
        if 500<=oraliq['price']<=1001 and oraliq['is_available'] :
            print(f"{oraliq['id']} = {oraliq['price']}" ) 
    