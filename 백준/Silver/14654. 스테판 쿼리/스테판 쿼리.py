N = int(input())

continous = 0
cnt = 0
prev = ""

for A, B in zip(list(map(int, input().split())), list(map(int, input().split()))):
    if A == B:
        prev = "A" if prev == "B" else "B"
        cnt = 1
    elif (
        (A == 1 and B == 3) 
        or (A == 2 and B == 1)
        or (A == 3 and B == 2)
    ):
        if prev == "A": cnt += 1
        else: prev, cnt = "A", 1
    else:
        if prev == "B": cnt += 1
        else: prev, cnt = "B", 1

    continous = max(cnt, continous)

print(continous)