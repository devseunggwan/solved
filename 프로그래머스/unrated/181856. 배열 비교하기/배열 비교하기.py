def solution(arr1, arr2):
    answer = 0
    l = len(arr1) - len(arr2)
    s = sum(arr1) - sum(arr2)
    
    if (l == 0 and s > 0) or l > 0:
        answer = 1
    elif (l == 0 and s < 0) or l < 0:
        answer = -1

    return answer