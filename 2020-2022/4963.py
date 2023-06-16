'''
구현 전략
* BFS(breadth first search)를 사용한다.
* 기존 맵과 맵 체크 배열을 만든다.
* 맵을 돌면서 순회한 곳은 체크한다.
'''

while True:
    W, H = map(int, input().strip().split())
    if(W == 0 and H == 0): break

    ans = 0
    C = [[0 for i in range(W)] for j in range(H)]
    M = [list(map(int, input().strip().split())) for i in range(H)]

    for i in range(H):
        for j in range(W):
            pass
