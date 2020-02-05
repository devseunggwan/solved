N, K = map(int, input().strip().split())
if(K > N or K < 0): print(0)
else:
	n, k, m = 1, 1, 1
	for i in range(1, N+1): n*=i
	for i in range(1, K+1): k*=i
	for i in range(1, N-K+1): m*=i

	print(int(n/(k*m))) 