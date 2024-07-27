from collections import deque


N = int(input())
queue = deque()

for i in range(N, 0, -1):
    queue.appendleft(str(i))
        
    for j in range(i):
        queue.appendleft(queue.pop())        
               
print(" ".join((queue)))