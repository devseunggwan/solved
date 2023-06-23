def solution(num_list):
    answer = -1
    
    for idx, num in enumerate(num_list):
        if num < 0:
            answer = idx
            break
    
    return answer