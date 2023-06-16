numbers = int(input())
number = 10000
Nodes = [[0]*number for i in range(number)]
Checks = Nodes

for i in range(numbers-1):
	A, B = map(int, input().strip().split())
	Nodes[A-1][B-1], Nodes[B-1][A-1] = 1, 1

def dfs(start:int, Nodes:list, Checks:list, Road: list, result: list):
	for i in range(len(Nodes)):
		if(Nodes[start][i] is 1 and Checks[start-1][i] is 0 and i+1 not in Road):
			Checks[start][i] = 1
			Road.append(i+1)
			result.append([start+1, i+1])
			dfs(i, Nodes, Checks, Road, result)
		if(len(Nodes) == len(Road)): break
	return result

R = sorted(dfs(0, Nodes, Checks, [1], list()), key=lambda x: x[:][1])

for i in range(len(R)): print(R[i][0])