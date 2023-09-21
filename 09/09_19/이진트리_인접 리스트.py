arr = [1,2,1,3,2,4,3,5,3,6]
nodes = [[] for _ in range(1,14)]

def preorder(nodeNumber):
    if nodeNumber == None:
        return
    print(nodeNumber, end=" ")
    preorder(nodes[nodeNumber][0]) #첫번째로 append한 애기에 왼쪽임
    # print(nodeNumber, end=" ") 중위
    preorder(nodes[nodeNumber][1])
    # print(nodeNumber, end=" ") 후위


for i in range(0,len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].append(childNode)
    # 트리에서는 부모에서 자식으로 가는 경우가 거의 대부분임.
    # 따라서 반대를 저장할 필요가 거의 없음..

# 자식이 더이상 없다는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li),2):
        li.append(None)

preorder(1)