def solution(arr, query):
    for idx, q in enumerate(query):
        arr = arr[q:] if idx % 2 else arr[:q+1]
        
    return arr