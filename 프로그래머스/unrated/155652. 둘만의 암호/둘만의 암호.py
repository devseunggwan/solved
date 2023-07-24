def convert_num(sentence):
    return list(map(lambda x: ord(x) - 97, list(sentence)))

def convert_rule(s, skip, index):
    while index:
        s = (s + 1) % 26
        if s not in skip:
            index -= 1
    
    s = chr(s + 97)
    
    return s

def solution(sentence, skip, index):
    sentence = convert_num(sentence)
    skip = convert_num(skip)
    index = index % (26 - len(skip))
        
    return ''.join([convert_rule(s, skip, index) for s in sentence])