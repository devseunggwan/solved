def solution(arr, flags):
    answer = []
    
    for num, flag in zip(arr, flags):
        if flag:
            answer.extend([num] * num * 2)
        else:
            answer = answer[:(-num)]
    
    return answer