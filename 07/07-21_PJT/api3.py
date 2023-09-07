import json
import requests

# 날씨 api가져오기
# api 사용량 제한 // 분당 60번, 1,000,000번 / 한달 제한

API_KEY = "5310463b07693b401bc5cb3c5967c297"
CITY = "Tokyo,JP"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={37.56}&lon={126.97}&appid={API_KEY}"
url2 = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

data = requests.get(url).json()
data_for_respon = requests.get(url)
data_for_Japan = requests.get(url2).json()
print(data,end="\n-----------------------------------------\n\n")
# print(data_for_respon)
print(f"{float(data['main']['temp']) - 273.15:.2f}",end="\n-----------------------------------------\n\n")
print(data_for_Japan,end="\n-----------------------------------------\n\n")
print(data['weather'][0]['description'])