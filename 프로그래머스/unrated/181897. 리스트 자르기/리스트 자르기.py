def solution(n, slicer, num_list):
    funcs = {
        1: lambda num_list, a, b, c: num_list[:b+1],
        2: lambda num_list, a, b, c: num_list[a:],
        3: lambda num_list, a, b, c: num_list[a:b+1],
        4: lambda num_list, a, b, c: num_list[a:b+1:c],
    }
    a, b, c = slicer
    
    return funcs[n](num_list, a, b, c)