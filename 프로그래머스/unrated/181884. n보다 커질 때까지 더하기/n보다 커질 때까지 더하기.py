def solution(numbers, n):
    answer = 0
    
    for number in numbers:
        answer += number
        if answer > n:
            break
        
    return answer