M, N, P, Q = int(input()), int(input()), 0, 0

if(M-N == 0 and int(M**0.5)**2 == M): 
	P, Q = M, M
	print(Q)
	print(P)
elif(M-N == 0 or int(N**0.5)-int(M**0.5) == 0): print(-1)
elif(int(M**0.5)**2 == M):
	P = M
	for i in range(int(M**0.5), int(N**0.5)+1): Q+=i**2
	print(Q)
	print(P)
else:
	P = (int(M**0.5)+1)**2
	for i in range(int(M**0.5)+1, int(N**0.5)+1): Q+=i**2
	print(Q)
	print(P)