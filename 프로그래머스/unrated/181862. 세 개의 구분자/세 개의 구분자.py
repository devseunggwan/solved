def solution(myStr):
    answer = []
    temp = ""
    
    for s in myStr:
        if s in ["a", "b", "c"]: 
            if temp != "":
                answer.append(temp)
                temp = ""
        else:
            temp += s            
    
    if temp:
        answer.append(temp)
    if not answer:
        answer.append("EMPTY")
    
    return answer