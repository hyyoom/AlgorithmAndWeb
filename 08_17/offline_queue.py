class MyQueue:
    
    
    # 자료를 저장하기위한 공간
    def __init__(self, N):
        self.queue = [None] * N
        self.front = -1
        self.rear = -1
    
    
    # q 데이터 삽입
    def en_queue(self, data):
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear] = data
        else:
            print("큐가 가득 참")
    


    # q에서 삭제 및 출력
    def de_queue(self):
        if not self.is_empty():
            self.front += 1
            return self.queue[self.front]
        else:
            print("큐가 빔")


    def is_full(self):
        if self.rear == len(self.queue) - 1:
            return True
        return False

    
    def is_empty(self):
        if self.rear == self.front:
            return True
        return False


queue = MyQueue(5)

queue.en_queue(5)
queue.en_queue(4)
queue.en_queue(3)
queue.en_queue(2)
queue.en_queue(1)

print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())

# 1. 서류

# 월세 계약서, 가족관계증명서 

# 본인, 부, 모 가족관계증명서 상세 가구원전체 주민번호 뒷자리까지
# 7월, 8월 월세 이체내역 보내는사람 받는사람다 확인되어야함
# 이체확인증이나, 송금확인증 확인 (폰으로 가능) 두달치 월세
# 온라인에는 본인명의 통장사본 첨부x 

# 신청 온라인으로 하면 
# 원가구 등록 = 부모님 등록 해야함/ 
# 8 21까지 신청

# lh전세 전입신고


# 2. 기한




