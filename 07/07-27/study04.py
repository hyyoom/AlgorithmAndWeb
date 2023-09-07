


class Cat:
    def __init__(self):
        self.sound = "야옹"


class Dog:
    def __init__(self):
        self.sound = "멍멍"


class Pet(Cat, Dog):
    def __init__(slef):
        super().__init__()

    def __str__(self):
        return f"애완동물은 {self.sound} 소리를 냅니다."

pet1 = Pet()
print(pet1,end="")

