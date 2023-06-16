chk = [input() for i in range(5)]
chk_len = [len(i) for i in chk]
al = ""

for i in range(max(chk_len)):
	for j in range(5):
		if(i< chk_len[j]): al+=chk[j][i]

print(al)