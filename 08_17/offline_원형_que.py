class MyQueue2: # 원형큐
    def __init__(self, N) -> None:
        self.queue = [None] * N
        self.front = self.rear = 0
    

    def en_queue(self, data):
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data
        else:
            print("가득 참")

    def de_queue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]
        else:
            print("비었음")


    def if_full(self):
        # rear의 다음칸이 front라면
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        return False

    
    def is_empty(self):
        if self.front == self.rear:
            return True
        return False