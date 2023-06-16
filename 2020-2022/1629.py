A, B, C = map(int, input().split())


def sol(A, B):
    if(B == 0):
        return 1
    elif(B == 1):
        return A
    elif(B % 2 > 0):
        return sol(A, B-1) * A
    else:
        return ((sol(A, B // 2) % C) ** 2) % C


print(sol(A, B) % C)
