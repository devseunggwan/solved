def solution(q, r, code):
    return ''.join([x for idx, x in enumerate(code) if idx % q == r])