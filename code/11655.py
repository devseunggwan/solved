def ROT13(M: str):
    for i in M:
        if i.islower():
            print(chr(96 + ((ord(i) - 96 + 13) % 26)), end="")
        elif i.isupper():
            print(chr(64 + ((ord(i) - 64 + 13) % 26)), end="")
        else:
            print(i, end="")


ROT13(input())
