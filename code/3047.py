D = dict()
D["A"], D["B"], D["C"] = sorted(map(int, input().strip().split()))
print(*[D[i] for i in input()])