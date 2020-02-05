voca = [input() for i in range(int(input()))]
ans = ""

for i in range(len(voca[0])):
	for j in range(len(voca)):
		if(voca[j][i] != voca[0][i]): 
			ans+="?"
			break
		elif(len(voca)-1 == j): 
			ans += voca[0][i]
			break

print(ans)