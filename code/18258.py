import sys
from collections import deque

queue = deque()
for i in range(int(sys.stdin.readline())):
    query = sys.stdin.readline()
    if("push" in query):
        query = query.strip().split()
        queue.append(query[1])
    elif("pop" in query):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue.popleft())
    elif("size" in query):
        print(len(queue))
    elif("empty" in query):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif("front" in query):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif("back" in query):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])
