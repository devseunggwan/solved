N = int(input())
M = list(map(int, input().strip().split()))
M.sort()

start = 0
end = N - 1
value = 2_000_000_000
answer = (1_000_000_000, 1_000_000_000)

while start != end:
    if abs(M[start] + M[end]) <= abs(sum(answer)):
        answer = (M[start], M[end])

    if M[start] + M[end] > 0:
        end -= 1
    elif M[start] + M[end] < 0:
        start += 1
    else:
        break


print(" ".join(map(str, answer)))