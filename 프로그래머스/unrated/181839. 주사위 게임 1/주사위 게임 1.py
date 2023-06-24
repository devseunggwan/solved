def solution(a, b):
    func = {
        2: lambda a, b: a ** 2 + b ** 2,
        1: lambda a, b: 2 * (a + b),
        0: lambda a, b: abs(a - b)
    }
    
    
    return func[sum([a % 2, b % 2])](a, b)