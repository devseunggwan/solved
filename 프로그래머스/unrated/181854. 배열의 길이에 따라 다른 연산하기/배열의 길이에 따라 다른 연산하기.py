def solution(arr, n):
    l = len(arr) % 2
    return [num + (n if idx % 2 ^ l else 0) for idx, num in enumerate(arr)]