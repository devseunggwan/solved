def solution(arr):
    row, col = len(arr[0]), len(arr)
    
    if row < col:
        arr = [r + [0] * (col - row) for r in arr]
    elif row > col:
        for i in range(row - col):
            arr.append([0] * row)
    
    return arr