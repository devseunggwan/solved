def solution(myString, pat):
    answer = ''
    
    for idx in range(len(myString)-len(pat)+1):
        if myString[idx:idx+len(pat)] == pat:
            answer = myString[:idx+len(pat)]
    
    return answer