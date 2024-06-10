def agg(survey: list, choices: list) -> dict:
    M = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }
    
    for svy, choice in zip(survey, choices):
        nagative, positive = svy
        
        if choice in [1, 2, 3]:
            M[nagative] += 4 - choice
        elif choice in [5, 6, 7]:
            M[positive] += choice - 4

    return M


def solution(survey: list, choices: list):
    agg_map = agg(survey, choices)

    M = "R" if agg_map["R"] >= agg_map["T"] else "T"
    B = "C" if agg_map["C"] >= agg_map["F"] else "F"
    T = "J" if agg_map["J"] >= agg_map["M"] else "M"
    I = "A" if agg_map["A"] >= agg_map["N"] else "N"
    
    
    return M + B + T + I