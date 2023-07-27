# 다중 상속
# 여러개의 클래스를 상속 받을시 중독된 메서드가 있을때, 먼저 받은 클래스의 메서드, 속성을 가져옴

class Person:
    gene = "XYZ"

    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(f"{self.name}")


class Mom(Person):
    gene = "XX"

    def swim(self):
        return "엄마가 수영"


class Dad(Person):
    gene = "XY"
    
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def swim(self):
        return "아빠가 수영"

    def walk(self):
        return "아빠가 걷기"


class FirstChild(Mom, Dad):
    #dad의 유전자 정보를 저장하고 싶다면
    dad_gene = Dad.gene
    # def swim(self):
    #     return "첫째가 수영"
    def __init__(self, name, age):
        # super().__init__(name)
        Dad.__init__(self, name, age)

    def cry(self):
        return "첫째가 움"
    


baby1 = FirstChild("애기", 1)
print(baby1.cry())
print(baby1.swim())
print(baby1.gene)
print(baby1.dad_gene) # 다중 상속에서 상위의 상위 클래스처럼 위의 클래스의 속성을, 메서드를 찾기 위해

print(FirstChild.mro()) # 클래스 탐색의 순서 super는 이 순서대로 찾아 옴
