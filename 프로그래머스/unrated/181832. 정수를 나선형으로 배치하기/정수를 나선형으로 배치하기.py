def solution(n):
    map_list = [[0] * n for i in range(n)]
    map_step = [
        [0, 1], [1, 0], [0, -1], [-1, 0]
    ]
    
    cur = [0, 0]
    flag = 0
    
    for i in range(1, n * n + 1):
        map_list[cur[0]][cur[1]] = i

        if not (0 <= cur[0] + map_step[flag][0] < n) or not (0 <= cur[1] + map_step[flag][1] < n):
            flag = 0 if flag + 1 >= 4 else flag + 1
        elif map_list[cur[0] + map_step[flag][0]][cur[1] + map_step[flag][1]] != 0:
            flag = 0 if flag + 1 >= 4 else flag + 1

        cur[0], cur[1] = cur[0] + map_step[flag][0], cur[1] + map_step[flag][1]
        
    return map_list
    