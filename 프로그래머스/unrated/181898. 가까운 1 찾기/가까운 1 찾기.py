def solution(arr, idx):
    return (-1 if 1 not in arr[idx:] else idx + (arr[idx:]).index(1))