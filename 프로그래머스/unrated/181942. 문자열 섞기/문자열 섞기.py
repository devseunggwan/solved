def solution(str1, str2):
    return "".join([s1 + s2 for s1, s2 in zip(str1, str2)])