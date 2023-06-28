def solution(date1, date2):
    date1[1] = str(date1[1]).rjust(2, "0")
    date2[1] = str(date2[1]).rjust(2, "0")
    
    date1 = int(''.join(map(str, date1)))
    date2 = int(''.join(map(str, date2)))

    return int(date1 < date2)