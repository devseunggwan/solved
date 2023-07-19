s = input()
res = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        res.append("".join([k[::-1] for k in [s[:i], s[i:j], s[j:]]]))

print(sorted(res)[0])
