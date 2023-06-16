import sys

cod = 0
cnt = int(input())
for i in range(cnt):
    cod += int(sys.stdin.readline().strip().split()[0])-1
print(cod+1)
