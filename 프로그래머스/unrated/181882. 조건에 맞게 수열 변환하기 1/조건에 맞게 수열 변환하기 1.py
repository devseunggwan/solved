

def solution(arr):
    answer = []
    
    for n in arr:
        if n >= 50 and n % 2 == 0:
            n = n/2
        elif n < 50 and n % 2 != 0:
            n = n*2
        
        answer.append(n)
        
    return answer