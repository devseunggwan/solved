N, m, M, T, R = map(int, input().split())

a = m
answer = 0

if T > M - m:
    answer = -1
else:
    while N:    
        if a + T <= M:
            N, a = N - 1, a + T
        else:
            if a - R < m:
                a = m
            else:
                a -= R

        answer += 1
    
print(answer)