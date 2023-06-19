def solution(t, p):
    return len([1 for num in range(len(t)-len(p)+1) if int(t[num:num+len(p)]) <= int(p)])