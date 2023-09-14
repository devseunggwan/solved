node = int(input())
edge = int(input())

# map 생성
nodes = [[0 for i in range(node)] for j in range(node)]

# 간선 위치 체크
for i in range(edge):
	x, y = map(int, input().split())
	nodes[x-1][y-1], nodes[y-1][x-1] = 1, 1

#dfs
def DFS(map: list, hive: int, infestion: list)->int:
	for i in range(len(map)):
		# 간선이 연결되어 있고, 노드 순회를 하지 않은 경우, 해당 노드를 경로에 추가하고 연결된 노드 탐색  
		if(map[hive-1][i] == 1 and i+1 not in infestion):
			infestion.append(i+1)
			DFS(map, i+1, infestion)
		#노드를 전부 순회한 경우 루프 탈출
		if(len(infestion) == len(map)): break
	return len(infestion)

print(DFS(nodes, 1, [1])-1)