
# 실습 번호.py
number_of_people = 100
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

def decrease_book(num,na):
    global number_of_book

    number_of_book -= num

    print(f"남은 책의 수 :  {number_of_book}")
    print(f"{na}님이 {num} 권의 책을 대여했습니다")

my_dict = list(zip(name, age))

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(el):
    new_dict = {}
    new_dict["name"] = el[0]
    new_dict["age"] = el[1]
    return new_dict


def rental_book(info):
    n = info["age"] // 10
    na = info["name"]
    return decrease_book(n,na)
    # return decrease_book(n)

def fun1(info):
    return info["name"]

# many_user = list(map(create_user,my_dict))
many_user = list(map(lambda el: {"name": el[0], "age": el[1]}, my_dict))


b = list(map(fun1, many_user))
for i in b:
    print(f"{i}님 환영합니다 !")
a = list(map(rental_book, many_user))


