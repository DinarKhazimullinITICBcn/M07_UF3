import json
with open("llibres.json", 'r') as file:
    result = json.load(file)
    print(result)