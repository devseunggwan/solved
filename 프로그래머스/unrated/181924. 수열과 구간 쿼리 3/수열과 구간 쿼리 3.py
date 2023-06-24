def solution(arr, queries):    
    for idx1, idx2 in queries:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    
    return arr