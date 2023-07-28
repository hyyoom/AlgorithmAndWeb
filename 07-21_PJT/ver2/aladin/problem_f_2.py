import json


def sorted_cs_books_by_price(books, categories):
    # print(books)
    ret = []
    com_id = 0

    for i in range(len(categories)):
        if categories[i]["name"] == "컴퓨터 공학":
            com_id = categories[i]['id']
    
    for i in range(len(books)):
        for j in range(len(books[i]["categoryId"])):
            if books[i]["categoryId"][j] == com_id:
                    ret.append(books[i]["title"])
    return ret


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
