from collections import Counter, deque

N = list(map(int, input().strip().split()))
S = [range(1, N[i] + 1) for i in range(3)]

dq = deque()

for i in S[0]:
    for j in S[1]:
        for k in S[2]:
            dq.append(i + j + k)

C = Counter(dq).most_common()

print(C[0][0])
