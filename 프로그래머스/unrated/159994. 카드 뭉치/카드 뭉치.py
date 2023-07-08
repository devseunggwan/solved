from collections import deque

def solution(cards1, cards2, goal):
    is_make_goal = True
    cards1, cards2 = deque(cards1), deque(cards2)
    
    for g in goal:
        if cards1 and g == cards1[0]: cards1.popleft()
        elif cards2 and (g == cards2[0]): cards2.popleft()
        else:
            is_make_goal = False
            break
    
    return "Yes" if is_make_goal else "No"