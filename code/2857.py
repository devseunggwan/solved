ans = list()
for i in range(1, 6):
    if "FBI" in input():
        ans.append(i)

if len(ans) > 0:
    print(*ans)
else:
    print("HE GOT AWAY!")
