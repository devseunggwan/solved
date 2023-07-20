from typing import List, Tuple

def preprocessing_input_data() -> List[Tuple[int, int]]:
    """
    * A1, B2, C3 등 데이터를 [(x, y), ...] 형태로 변경합니다.
    
    Return
        List[Tuple(int, int)]
    """
    input_cnt = 36
    convert_xy_format = lambda x: (ord(x[0])-65, int(x[1])-1)
    
    return [list(map(convert_xy_format, input().strip().split()))[0] for _ in range(input_cnt)]

def chess_knight_tour(path: List[Tuple[int, int]]) -> str:
    """
    * Path에 따라서 나이트를 순회합니다.
    
    Parameter
        * path (list[tuple(int, int)]): 나이트가 순회할 경로, tuple 당 (x, y) 형태로 제공되어야 합니다. 
    
    Return
        str
            * Valid: 순회가 되는 경우
            * Invalid: 순회가 되지 않는 경우
    """
    M = [[0] * 6 for _ in range(6)]
    res = "Valid"
    
    # Path를 순회하면서 말이 갈 수 있는 곳인 지 확인
    for idx in range(36):
        x, y = path[idx]

        if idx == 0:
            M[x][y] = 1
            prev_x, prev_y = path[idx]
            continue
        
        if sorted([abs(prev_x - x), abs(prev_y - y)]) != [1, 2] or M[x][y]:
            res = "Invalid"
            break
        else:
            M[x][y] = 1
            prev_x, prev_y = path[idx]
    
    # 마지막에 방문한 칸에서 시작점으로 돌아올 수 잇는 지 체크
    if sorted([abs(path[0][0] - path[35][0]), abs(path[0][1] - path[35][1])]) != [1, 2]:
        res = "Invalid"
            
    return res  

def run():
    path = preprocessing_input_data()
    return chess_knight_tour(path)

if __name__ == "__main__":
    print(run())