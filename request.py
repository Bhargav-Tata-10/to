import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Enter the text':"What's happening"})

print(r.json())
