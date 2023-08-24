import sys
from collections import deque

# 1. 입력 불러오기
R = lambda: sys.stdin.readline()
N = int(R())
M = {}
for A, B in [map(int, R().split()) for _ in range(N-1)]:
    if not M.get(A):
        M[A] = [B]
    else:
        M[A].append(B)
    
    if not M.get(B):
        M[B] = [A]
    else:
        M[B].append(A)
    
# 2. 인접 리스트 및 구조체 선언
T = {1: []}
queue = deque([1]) # 부모 노드에서 찾은 노드들을 추가하여 큐로 찾을 수 있게 함
answer = [0] * (N+1)

# 3. 부모 노드 순회하면서 자식 노드 찾기 (BFS)
while queue:
    parent = queue.popleft()
    for child in M[parent]:
        if not answer[child]:
            answer[child] = parent
            queue.append(child)
            
# 4. 정답 출력
for idx in range(2, N+1):
    print(answer[idx])
