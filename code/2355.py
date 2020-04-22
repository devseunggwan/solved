A = list(map(int, input().strip().split()))
A.sort()
print(int((A[1]+A[0])*((A[1]-A[0] + 1))/2))
