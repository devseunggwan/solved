def solution(wallpaper):
    answer = [None, None, None, None]

    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == ".":
                continue
            
            answer[0] = y if answer[0] is None else min(y, answer[0])
            answer[1] = x if answer[1] is None else min(x, answer[1])
            answer[2] = y + 1 if answer[2] is None else max(y + 1, answer[2])
            answer[3] = x + 1 if answer[3] is None else max(x + 1, answer[3])

    return answer