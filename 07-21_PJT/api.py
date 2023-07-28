import requests

url = 'https://fakestoreapi.com/carts'

data = requests.get(url).json() # 데이터
respons = requests.get(url)     # 응답코드 

print(respons)
print(data)