def func(x, k):
    if k % 2 == 0:
        return x + k
    else:
        return x * k

def solution(arr, k):
    return list(map(lambda x: func(x, k), arr))