X, Y = map(str, input().strip().split())


def Rev(S):
    num = ""
    for i in S:
        num = i + num

    return num


print(int(Rev(str(int(Rev(X)) + int(Rev(Y))))))
