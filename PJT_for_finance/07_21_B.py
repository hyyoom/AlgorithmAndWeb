import pprint
import requests
# 5037c8fbe58a7bb21ce43062eceb8d1d

# ppt를 대충 훑고 시작해서 엉뚱한 API_KEY를 가져왔고 url을 못 찾아서 시간을 많이 날렸다.
# data['result'].keys() 부분을 생각하는데 오래걸렸다. 해당 공식문서를 제대로 읽지 않아서
# 계속 data.keys()로 검색했고 result라는 문장만 키로 나왔기에 이걸 해결하는데 오래걸렸다.


def get_deposit_products():
    API_KEY = "fdfdd16a3d1fccb9ac34750dba395ea7"
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    data = requests.get(url).json()
    result = data['result'].keys()
    print(data["products"])
    # print(data['result']["baseList"])
    
    return result




# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)