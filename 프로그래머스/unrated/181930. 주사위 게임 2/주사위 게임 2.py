from collections import Counter

def solution(a, b, c):
    func = {
        1: lambda a, b, c: (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3),
        2: lambda a, b, c: (a + b + c) * (a ** 2 + b ** 2 + c ** 2),
        3: lambda a, b, c: (a + b + c)
    }
    
    return func[len(Counter([a, b, c]))](a, b, c)