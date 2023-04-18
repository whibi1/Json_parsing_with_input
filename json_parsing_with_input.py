import json
import urllib.request

def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data

def extract_data(data, key):
    if key in data:
        return data[key]
    elif isinstance(data, dict):
        for k, v in data.items():
            item = extract_data(v, key)
            if item is not None:
                return item
    elif isinstance(data, list):
        for item in data:
            result = extract_data(item, key)
            if result is not None:
                return result

url = input("Link of the Json: ")
data = fetch_data(url)
print(data)
key = input("Data name you want to export to text file: ")
result = extract_data(data, key)
print(result)
with open("data.txt","w",encoding="utf-8") as veri:
    veri.write(str(result))
    
