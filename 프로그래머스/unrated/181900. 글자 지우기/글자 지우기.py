def solution(my_string, indices):
    return ''.join([x for idx, x in enumerate(my_string) if idx not in indices])