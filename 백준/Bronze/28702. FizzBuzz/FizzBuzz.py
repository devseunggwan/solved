def read():
    M = [input() for _ in range(3)]

    for idx, i in enumerate(M):
        try:
            num = int(i) + (3 - idx)
            break
        except:
            pass

    return num


def fizzbuzz(num):
    return (
        ("Fizz" if num % 3 == 0 else "")
        + ("Buzz" if num % 5 == 0 else "")
        + (str(num) if num % 3 != 0 and num % 5 != 0 else "")
    )


if __name__ == "__main__":
    num = read()

    print(fizzbuzz(num))
