N, K = map(int, input().split())
A = [a for a in reversed([int(input()) for _ in range(N)]) if a <= K]

temp = []

for a in A:
    for i in range(len(temp)):
        case = temp[i]

        if case[0] != 0:
            temp.append((case[0] % a, case[1] + case[0] // a))

    temp.append((K % a, K // a))

temp = min([case[1] for case in temp if case[0] == 0])

print(temp)
