# 시간 초과로 인해 사용
import sys
r = lambda: sys.stdin.readline()

stack = list()
for loop in range(int(input())):
    queue = r()
    if("push" in queue):
        push, num = queue.strip().split()
        stack.append(int(num))
    elif("pop" in queue):
        if(stack == list()): print(-1)
        else: print(stack.pop(-1))
    elif("size" in queue): print(len(stack))
    elif("empty" in queue):
        if(len(stack) == 0): print(1)
        else: print(0)
    elif("top" in queue):
        if(len(stack) == 0): print(-1)
        else: print(stack[-1])