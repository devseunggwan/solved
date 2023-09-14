def solution():
    r = []
    for s in input().split():
        if s in r:
            return "no"
        r.append(s)
    
    return "yes"
    
print(solution())