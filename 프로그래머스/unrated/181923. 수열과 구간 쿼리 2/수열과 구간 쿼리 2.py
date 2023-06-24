def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = [num for idx, num in enumerate(arr) if s <= idx <= e and num > k]
        answer.append(min(temp) if temp != [] else -1)
        
    return answer