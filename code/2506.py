N = int(input())
ans, o = 0, 0

for i in map(int, input().strip().split()):
    if(i == 1):
        o += 1
        ans += o

    else:
        o = 0
print(ans)
