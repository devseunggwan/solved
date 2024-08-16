while True:
    sentence = input()

    if sentence == "***":
        break

    print("".join(list(sentence)[::-1]))
