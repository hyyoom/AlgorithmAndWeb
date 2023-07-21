import pprint
import requests
# 5037c8fbe58a7bb21ce43062eceb8d1d




def get_deposit_products():
    API_KEY = "fdfdd16a3d1fccb9ac34750dba395ea7"
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    data = requests.get(url).json()
    result = data['result'].keys()
    
    return result




# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)