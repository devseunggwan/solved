def solution(num_list):
    answer = 0
    func = lambda x: (x - (x % 2)) / 2 
    
    for num in num_list:
        while num != 1:
            num = func(num)
            answer += 1

    return answer