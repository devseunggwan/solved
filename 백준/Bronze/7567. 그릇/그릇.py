bowls = input()
print(sum([10 if bowls[idx-1] != bowls[idx] else 5 for idx in range(1, len(bowls))]) + 10)