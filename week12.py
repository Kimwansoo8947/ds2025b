from collections import deque # collections 라이브러리에 있음

d = deque([3,-9,14]) # 객체 생성
d.append(77)
# d.appendleft(100)
d.append(91)

for i in range(len(d)):
    print(d.popleft())