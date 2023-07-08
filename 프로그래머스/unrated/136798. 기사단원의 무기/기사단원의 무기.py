def moduler(num):
    count = 0
    t = []
    
    for idx in range(1, int(num ** 0.5)+1):
        if num % idx == 0:
            count += 1
            if (idx ** 2 != num):
                count += 1
                
    return count

def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        p = moduler(num)        
        answer += p if p <= limit else power
    
    return answer