import requests
import json

def call_API(foodName, apiKey):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={apiKey}&query={foodName}'
    res = requests.get(url)
    print(res.status_code)
    return res.json()

