import json

json_data = '''
{
    "name" : "유형민",
    "age" : 30
}
'''
data = json.loads(json_data) # 파이썬 딕셔너리로 반환
name = data.get('name')

print(data)
print(name)

# 문자열 -> dict -> data추출 
# 즉 파싱 과정 == 원하는 형태로 변환, 
# 데이터를 의미 있는 구조로 분석하고 해석하는 과정