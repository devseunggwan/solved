def solution(arr):
    answer = []
    
    for num in arr:
        answer.extend([num] * num)

    return answer