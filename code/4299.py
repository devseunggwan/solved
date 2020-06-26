S, M = map(int, input().strip().split())
if(S < M or (S+M)%2 == 1): print(-1)
else: print(*sorted([(S+M)//2, (S-M)//2], reverse=True))