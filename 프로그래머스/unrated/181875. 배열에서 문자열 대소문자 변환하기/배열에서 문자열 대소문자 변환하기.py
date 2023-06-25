def solution(strArr):
    return [s.upper() if idx % 2 else s.lower() for idx, s in enumerate(strArr)]