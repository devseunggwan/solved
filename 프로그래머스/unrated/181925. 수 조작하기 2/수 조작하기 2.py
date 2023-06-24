def solution(numLog):
    m = {
        1: "w",
        -1: "s",
        10: "d",
        -10: "a"
    }
        
    return "".join([m[s] for s in [numLog[i+1]-numLog[i] for i in range(0, len(numLog)-1)]])