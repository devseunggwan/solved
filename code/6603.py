from itertools import combinations
cnt = 0

while True:
    T = list(map(int, input().strip().split()))
    if(T == [0]): break
    if(cnt != 0): print("")
    P = list(combinations(T[1:], 6))
    for i in P: print(*i)
    cnt += 1