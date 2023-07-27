
class Cat:
    def __init__(self, meow):
        self.sound_cat = meow
    def __str__(self):
        return self.sound_cat


class Dog:
    def __init__(self, mung):
        self.sound_dog = mung
    def __str__(self):
        return self.sound_dog


class Pet(Dog, Cat):
    def __init__(self):
        Dog.__init__(self,"멍멍")
        Cat.__init__(self,"야옹")

    def __str__(self):
        dog_s = Dog.__str__(self)
        cat_s = Cat.__str__(self)
        return f"애완동물은 {dog_s} 소리를 냅니다.\n애완동물은 {cat_s} 소리를 냅니다."


dog1 = Dog("멍멍")
cat1 = Cat("야옹")

pet1 = Pet()
print(pet1,end="")