import sys

N = int(sys.stdin.readline())
stack = list()
answer = list()
flag = 0
roof = 1

for _ in range(N):
    number = int(sys.stdin.readline())
    while roof <= number:
        stack.append(roof)
        answer.append("+")
        roof += 1

    if stack[-1] == number:
        stack.pop()
        answer.append("-")

    else:
        print("NO")
        flag = 1
        break

if not flag:
    for i in answer:
        print(i)
