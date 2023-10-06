import matplotlib.pyplot as plt

# 예제1: x, y가 같을때
# plt.plot([1,2,3,4])
# plt.show()

#이때까지 그렸던 plt지우기
# plt.clf()
# 예제2: x, y가 다를때
x = [1,2,3,4]
y = [2,4,8,16]
plt.plot(x, y)
# 예제3: 제목 + 각 축의 설명
plt.title("TEST GRAPH")
plt.ylabel("y~")
plt.xlabel("x~")
# plt.show()
plt.savefig("filename.png") # plt.show하면 백지 저장됨

