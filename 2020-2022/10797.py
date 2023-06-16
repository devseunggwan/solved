stop = int(input())
num = [i for i in map(int, input().strip().split())]
result = 0
for i in num:
	if i%10 == stop : result+=1

print(result)