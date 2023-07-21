import json

#2023년 도서중 리뷰 평점이 가장 높은 도서 제목

def new_books(books):
    new_books = []

    for i in range(20):
        tmp = books[i]["id"]
        best_B = open(f'data/books/{tmp}.json', encoding='utf-8')
        best_B1= json.load(best_B)
        if best_B1["pubDate"][:4] == "2023":
            new_books.append([best_B1["customerReviewRank"], [best_B1["title"]]])

    return new_books

def best_new_books(books):
    book_year = new_books(books)
    tmp = book_year[0][0]
    for i in range(len(book_year)-1):
        if book_year[i][0] < book_year[i+1][0]:
            tmp = book_year[i+1][1]
    
    tmp = str(tmp)
    return tmp



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
