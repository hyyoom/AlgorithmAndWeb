# 0~9
# make set # 집합을 만듬
# 각 요소가 가리키는 값이 부모가 됨

parent = [i for i in range(10)]

# find set 부모를 찾아감
def find_set(x):
    if parent[x] == x: # c가 c를 가르키고 있다면
        return x
    
    parent[x] = find_set(parent[x]) # 경로 압축
    return parent[x]

# union 
def union(x, y):
    # 1.이미 같은 집합인지 체크
    # 2.다른 집합이라면, 같은 대표자로 수정

    x = find_set(x)
    y = find_set(y)
    if x == y: # 같은 집합이다
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

union(0,1)
union(2,3)
union(1,3)
# 대표자 검색
print(find_set(2))
print(find_set(0))


t_x = 0
t_y = 1

if find_set(t_x) == find_set(t_y):
    print("같은 집합")
else:
    print("다른 집합")
