from functools import reduce

def solution(num_list):
    return int(reduce(lambda x, y: x * y, num_list) < sum(num_list) ** 2)