ans = [0 for i in range(30)]

for i in range(28):
    ans[int(input()) - 1] = 1

for i in range(len(ans)):
    if(ans[i] == 0): print(i+1)