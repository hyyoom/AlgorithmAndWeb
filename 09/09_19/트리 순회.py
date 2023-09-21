arr = [1,2,1,3,2,4,3,5,3,6]

# 0. 이진 트리 저장
#  - 일차원 배열 저장 
# 1. 연결 리스트로 저장(코테x 개발용)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # 삽입 함수
    def insert(self, childNode):
        if not self.left:
            self.left = childNode
            return
        if not self.right:
            self.right = childNode
            return
        return
    # 순회
    def preorder(self):
        if self != None:
            # print(self.value, end='') 전위
            if self.left:
                self.left.preorder()
            # print(self.value, end='') 중위
            if self.right:
                self.right.preorder()
            # print(self.value, end='') 후위

# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(1,14)]
for i in range(0,len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()
# 2. 인접 리스트로 저장