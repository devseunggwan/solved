T = int(input().strip())
answer = ""

while T >= 9:
    T, answer = T // 9, str(T % 9) + answer

answer = str(T) + answer

print(answer)
