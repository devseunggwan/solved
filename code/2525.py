A, B = map(int, input().strip().split())
C = int(input())

print((A+((B+C)//60))%24, (B+C)%60)