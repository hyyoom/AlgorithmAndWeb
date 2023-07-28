import json
from pprint import pprint

# 반복문으로 해결할 방법을 찾아보려 했지만 오히려 더 하드코딩 식으로 될 것 같고,
# 방법도 찾지 못해서 하나하나 값을 넣었다.

def book_info(book):
    new_dic = {}
    new_dic["id"] = book["id"]
    new_dic["name"] = book["title"]
    new_dic['author'] = book['author']
    new_dic['priceSales'] = book['priceSales']
    new_dic['description'] = book['description']
    new_dic['cover'] = book['cover']
    new_dic['categoryId'] = book['categoryId']

    return new_dic
    # 여기에 코드를 작성합니다.  

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
