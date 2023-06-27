def solution(l, r):
    arr = ["5"]
    cur = 0
    
    for i in range(7):
        for j in range(cur, cur + (2 ** i)):
            arr.extend([arr[j] + "0", arr[j] + "5"])
    
        cur += 2 ** i

    arr = [num for num in map(int, arr) if l <= num <=r]
    
    return [-1] if not arr else arr