def deQ():
    global front
    if front == rear:
        print("Q is empty")
    else:
        front += 1
        return q[front]

def enQ(data):
    global rear
    if rear == Q_size-1:
        print("Q is full")   # 디버깅용
    else:
        rear+=1
        q[rear] = data

def isEmpty():
    return rear == front


def Qpeek():
    if isEmpty():
        print("Q empty")
    else:
        return q[front+1]



Q_size = 3
q = [0] * Q_size
front = -1
rear = -1

enQ(1)
enQ(2)
enQ(3)

print(Qpeek())
