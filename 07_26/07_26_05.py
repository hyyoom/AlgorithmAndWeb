# ws_7_5.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,wid,hei):
        self.wid = wid
        self.hei = hei
    
    def __str__(self):
        return f"shape: width={self.wid}, height={self.hei}"

shape1 = Shape(5, 3)
print(shape1)
