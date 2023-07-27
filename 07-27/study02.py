# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self):
        self.sound = "야옹 !"

class Cat(Animal):
    def __init__(self):
        super().__init__()


    def meow(self):
        print(self.sound)
        

cat1 = Cat()
cat1.meow()
