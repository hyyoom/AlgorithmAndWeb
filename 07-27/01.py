# 유연하지 않은 코드가 됨. (문제가 생겼을시 하위 클래스의 매개변수, 등을 다 바꿔야함)
# 다중 상속에서는 겹친다면 상속을 받는 순서대로 찾음

# 내장함수의 super()로 해결
# super() == 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f"안녕 {self.name}입니다")


class Professor(Person):
    def __init__(department):
        # Person.__init__(self, name, age)
        super().__init__(name, age) # self 사용하지 않음
        self.depar = department


class Student(Person):
    def __init__(self, name, age, gpa):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.gpa = gpa


p1 = Professor("박교수", 56, "컴공")
s1 = Student("김학생", 20, 3.5)


p1.talk()
s1.talk()



