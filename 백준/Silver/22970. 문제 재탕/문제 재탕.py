N = int(input())
A = list(map(int, input().strip().split()))

answer = 1
flag = False
length = 1

for i in range(N - 1):
    is_upper = A[i] < A[i + 1]

    if A[i] == A[i + 1]:
        length = 1
        continue

    if not flag and is_upper:
        length = 2
    else:
        length += 1

    flag = is_upper
    answer = max(length, answer)

print(answer)
