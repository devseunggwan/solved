def solution(a, d, included):
    return sum([res for res, b in zip(list(range(a, a + (len(included) * d) + 1, d)), included) if b])