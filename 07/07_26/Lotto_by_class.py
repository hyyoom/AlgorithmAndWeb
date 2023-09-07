# 로또 번호 만드는, 생성
# 로또 번호 정렬
# 로또 번호 만드는애가 정렬도 하면 == 클래스
import random

class LottoNumberMaker:

    def __init__(self):
        self.lotto_nums = []

    def create_number(self):
        while len(self.lotto_nums) < 6:
            ran_num = random.randint(1,45)
            self.lotto_nums.append(ran_num)

    def lotto_sort(self):
        self.lotto_nums.sort()

tmp = []
lotto1 = LottoNumberMaker()
lotto1.create_number()
lotto1.lotto_sort()
print(lotto1.lotto_nums)
