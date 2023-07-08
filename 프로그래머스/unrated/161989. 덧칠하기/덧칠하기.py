from collections import deque

def solution(n, m, section):
    answer = 0
    point = (0, 0)
    section = deque(section)
    
    while section:
        if not point[0] <= section[0] < point[1]:
            start = section.popleft()
            point = (start, start + m)
            answer += 1
        else:
            section.popleft()
    
    return answer