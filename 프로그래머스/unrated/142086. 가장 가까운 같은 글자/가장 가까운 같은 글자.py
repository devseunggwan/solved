def solution(s):
    spell_dict = {}
    answer = []
    
    for itr, spell in enumerate(s):
        if spell not in spell_dict:
            answer.append(-1)
            spell_dict[spell] = itr
        else:
            distance = itr - spell_dict[spell]
            answer.append(distance)
            spell_dict[spell] = itr
    
    return answer