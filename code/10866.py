import sys
import collections
deque = collections.deque()
for i in range(int(sys.stdin.readline())):
    query = sys.stdin.readline()
    if("push_front" in query):
        query = query.strip().split()
        deque.append(query[1])

    elif("push_back" in query):
        query = query.strip().split()
        deque.appendleft(query[1])
    elif("pop_front" in query):
        if(len(deque) == 0):
            print(-1)
        else:
            print(deque.pop())
    elif("pop_back" in query):
        if(len(deque) == 0):
            print(-1)
        else:
            print(deque.popleft())
    elif("size" in query):
        print(len(deque))
    elif("empty" in query):
        if(len(deque) == 0):
            print(1)
        else:
            print(0)
    elif("front" in query):
        if(len(deque) == 0):
            print(-1)
        else:
            print(deque[-1])
    elif("back" in query):
        if(len(deque) == 0):
            print(-1)
        else:
            print(deque[0])
