def ROT13(M: str):
    for i in M:
        if i.islower():
            print(chr(97 + ((ord(i) - 97 + 13) % 26)), end="")
        elif i.isupper():
            print(chr(65 + ((ord(i) - 65 + 13) % 26)), end="")
        else:
            print(i, end="")


ROT13(input())
