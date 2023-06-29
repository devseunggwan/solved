def solution(arr):
    answer = []
    
    if 2 not in arr:
        answer = [-1]
    else:
        start, end = 0, len(arr)-1
        
        for i in range(len(arr)):
            if arr[start] == 2:
                pass
            else:
                start += 1
            if arr[end] == 2:
                pass
            else:
                end -= 1
        
        answer = arr[start:end+1]
    
    return answer