D = dict()
for i in range(97, 97 + 26): D[chr(i)] = 0
for i in input(): D[i] += 1
print(*list(D.values()))