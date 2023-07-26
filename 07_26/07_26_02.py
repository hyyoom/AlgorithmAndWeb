# ws_7_2.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, wid,hei):
        self.wid = wid
        self.hei = hei
        self.perimeter = (self.wid * 2) + (self.hei * 2)
        self.area = wid * hei
    
    def print_info(self):
        print(f"width: {self.wid}")
        print(f"Height: {self.hei}")
        print(f"Area: {self.area}")
        print(f"Perimeter: {self.perimeter}")

        
shape1 = Shape(5, 3)
shape1.print_info()

