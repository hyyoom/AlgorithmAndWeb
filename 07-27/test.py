class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound
        
class Pet(Dog, Cat):
    def __init__(self, sound):
        Dog.__init__(self, sound)
        Cat.__init__(self, sound)

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

dog1 = Pet("멍멍")
cat1 = Pet("야옹")
print(dog1)
print(cat1)