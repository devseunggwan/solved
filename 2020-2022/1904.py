N = int(input())
DP = [1, 2]
for i in range(N-1): DP.append((DP[-1]+DP[-2])%15746)
print(DP[-2])