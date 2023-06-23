def solution(food):
    member1, member2 = '', ''
    
    food = [i//2 for i in food[1:]]
    
    for itr, food_cnt in enumerate(food):
        member1 += f"{itr+1}" * food_cnt
        member2 = f"{itr+1}" * food_cnt + member2
        
    return f"{member1}0{member2}"