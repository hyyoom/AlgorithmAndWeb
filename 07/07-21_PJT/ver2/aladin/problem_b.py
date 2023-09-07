import json
from pprint import pprint

tmp = []

# 요구사항을 헷갈려서 한참 돌아왔다.
# 포문 안에서 del new_dic을 불러와서 오류가 났는데 왜인지 몰라 한참 찾았다.

def book_info(book, categories_list):
    new_dic = {}
    new_dic["id"] = book["id"]
    new_dic["title"] = book["title"]
    new_dic['author'] = book['author']
    new_dic['priceSales'] = book['priceSales']
    new_dic['description'] = book['description']
    new_dic['cover'] = book['cover']
    new_dic['categoryId'] = book['categoryId']

    for i in new_dic['categoryId']:
        for j in range(len(categories_list)):
            if i == categories_list[j]["id"]:
                new_dic["categoryName"] = categories_list[j]["name"]
    del new_dic["categoryId"]
    
    return new_dic


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)
    # print(categories_list)
    # book_info(book, categories_list)
    pprint(book_info(book, categories_list))
