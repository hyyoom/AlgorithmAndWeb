import json




def best_book(books):
    best_B_list = [[] for i in range(20)]
    best_title = []

    for i in range(20):
        tmp = books[i]["id"]
        best_B = open(f'data/books/{tmp}.json', encoding='utf-8')
        best_B1= json.load(best_B)
        best_B_list[i] = best_B1["customerReviewRank"]
    maxv = max(best_B_list)
    for i in range(20):
        tmp = books[i]["id"]
        best_B = open(f'data/books/{tmp}.json', encoding='utf-8')
        best_B1= json.load(best_B)
        if best_B1["customerReviewRank"] == maxv:
            best_title.append(best_B1["title"])

    return best_title


        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))
