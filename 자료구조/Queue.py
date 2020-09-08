#deque 라이브러리를 통해 Queue 구현

from collections import deque


queue = deque()
#Queue는 선입선출을 지키는 '공평한' 자료구조
#=>먼저 들어온게 먼저 나간다.

queue.append(5)
queue.append(4)
queue.append(6)
queue.append(0)

queue.popleft() #위치와 상관없이 먼저 들어온 자료가 먼저 나간다.

queue.append(7)
queue.append(1)
queue.append(8)

queue.popleft()

queue.append(3)


print(queue)



