import json
from pprint import pprint


def books_info(books, categories_list):
    new_dic = [{} for i in range(20)]

    for i in range(20):
        new_dic[i]["id"] = books[i]["id"]
        new_dic[i]["title"] = books[i]["title"]
        new_dic[i]['author'] = books[i]['author']
        new_dic[i]['priceSales'] = books[i]['priceSales']
        new_dic[i]['description'] = books[i]['description']
        new_dic[i]['cover'] = books[i]['cover']
        new_dic[i]['categoryId'] = books[i]['categoryId']

        for k in new_dic[i]['categoryId']:
            for l in range(len(categories_list)):
                if k == categories_list[l]["id"]:
                    new_dic[i]["categoryName"] = categories_list[l]["name"]
        del new_dic[i]["categoryId"]
    
    return new_dic
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))