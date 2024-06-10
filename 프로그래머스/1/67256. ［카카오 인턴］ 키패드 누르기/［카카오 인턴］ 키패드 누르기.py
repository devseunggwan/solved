def get_distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1]) 

def solution(numbers, hand):
    answer = ''
    hand = hand.upper()[0]
    
    PHONE = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }
    
    state = {
        "L": [3, 2],
        "R": [3, 0]
    }
    
    for number in numbers:
        l = PHONE[number]
        
        if number in [1, 4, 7]:
            state["L"] = l
            answer += "L"
        elif number in [3, 6, 9]:
            state["R"] = l
            answer += "R"
        else:
            l_distance = get_distance(l, state["L"])
            r_distance = get_distance(l, state["R"])
        
            if l_distance == r_distance:
                state[hand] = l                    
                answer += hand
                
            elif l_distance < r_distance:
                state["L"] = l
                answer += "L"
            else:
                state["R"] = l
                answer += "R"

    return answer