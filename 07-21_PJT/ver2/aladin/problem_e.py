import json



def new_books(books):
    new_books = []

    for i in range(20):
        tmp = books[i]["id"]
        best_B = open(f'data/books/{tmp}.json', encoding='utf-8')
        best_B1= json.load(best_B)
        if best_B1["pubDate"][:4] == "2023":
            new_books.append(best_B1["title"])
    return new_books
    




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
