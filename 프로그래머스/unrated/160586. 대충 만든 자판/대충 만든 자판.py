def solution(keymap, targets):
    answer = []    
    dict_keymap = {}
    
    
    for key in keymap:
        for idx, k in enumerate(key):
            idx = idx + 1
            if k not in dict_keymap or min(dict_keymap[k], idx) == idx:
                dict_keymap[k] = idx
    
    for target in targets:
        click = 0    
        for t in target:
            if t not in dict_keymap:
                click = -1
                break
            
            click += dict_keymap[t]
    
        answer.append(click)
    
    return answer