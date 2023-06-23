def get_bin_map(arr_list, n):
    return [list(map(int, list(str(bin(arr))[2:].rjust(n, "0")))) for arr in arr_list]

def solution(n, arr1, arr2):
    answer = []
    
    arr1 = get_bin_map(arr1, n)
    arr2 = get_bin_map(arr2, n)
    
    for arr1_row, arr2_row in zip(arr1, arr2):
        arr_sum = ""
        for arr1_flag, arr2_flag in zip(arr1_row, arr2_row):
            arr_sum += "#" if arr1_flag + arr2_flag else " "
        
        answer.append(arr_sum)
        
        
    return answer