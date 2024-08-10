input()

stack = 0

while True:
    S = input()

    if S == "문제":
        stack += 1
    elif S == "고무오리" and stack == 0:
        stack += 2
    elif S == "고무오리":
        stack -= 1
    else:
        break

print("고무오리야 사랑해" if not stack else "힝구")
