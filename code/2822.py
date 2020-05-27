L = sorted([[int(input()), i] for i in range(1, 9)], key=lambda x: x[0])
ans = ["", 0]
for i in sorted(L[-5:], key=lambda x: x[1]):
    ans[0] += "{} ".format(i[1])
    ans[1] += i[0]

print(ans[1])
print(ans[0].strip())
