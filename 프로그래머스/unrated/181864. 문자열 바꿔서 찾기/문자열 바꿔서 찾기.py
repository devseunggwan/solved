def solution(myString, pat):
    return int(pat in "".join(["A" if s == "B" else "B" for s in myString]))