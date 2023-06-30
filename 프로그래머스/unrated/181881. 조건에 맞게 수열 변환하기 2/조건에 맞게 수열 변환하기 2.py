def condition(x):
    if x >= 50 and x % 2 == 0:
        return x / 2
    elif x < 50 and x % 2 == 1:
        return (x * 2) + 1
    else:
        return x

def solution(arr):
    answer = -1
    temp = []
    
    while arr != temp:
        temp, arr = arr, list(map(condition, arr))
        answer += 1
    
    return answer