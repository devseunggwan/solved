def solution(arr):
    stk = []
    
    for i, num in enumerate(arr):
        if not stk:
            stk.append(num)
        elif stk[-1] == num:
            stk.pop()
        elif stk[-1] != num:
            stk.append(num)
    
    return stk if stk else [-1]