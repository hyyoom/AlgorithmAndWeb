class Animal:
    num_of_animal = 0


class Cat:
   def meow(self):
        print("야옹 !\n",end="")


class Dog:
   def bark(self):
        print("멍멍 !\n",end="")


class Pet(Dog, Cat):

    def __init__(self,gg):
        self.gg = gg

    def make_sound(self):
        print(self.gg)
    
    def play(self):
        print("애완동물과 놀기", end="")

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()