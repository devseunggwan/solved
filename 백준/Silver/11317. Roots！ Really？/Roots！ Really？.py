for _ in range(int(input())):
    a, b, c, s, t = map(int, input().split())

    if ((b ** 2) - (4 * a * c)) < 0:
        print("No")
        continue    

    is_root = any(
        [
            s <= ((-b + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)) <= t,
            s <= ((-b - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)) <= t
        ]
    )

    print("Yes" if is_root else "No")