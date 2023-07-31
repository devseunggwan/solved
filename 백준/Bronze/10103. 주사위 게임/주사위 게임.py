A, B = 100, 100

for n in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif a < b:
        A -= b

print(f"{A}\n{B}")
