def solution(intStrs, k, s, l):
    return [int(strnum[s:s+l]) for strnum in intStrs if int(strnum[s:s+l]) > k]