while True:
    N = input()
    if N == "0 0":
        break
    
    A, B = map(int, N.split())
    
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")