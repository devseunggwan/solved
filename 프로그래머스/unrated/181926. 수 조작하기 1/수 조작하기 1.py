def solution(n, control):
    control_map = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    
    return n + sum([control_map[key] for key in control])