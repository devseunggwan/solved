def func(sentence: str) -> str:
    assert len(sentence) != 0
    
    res: str = ""
    
    for spell in sentence:    
        if spell.isupper():
            res += spell.lower()
        else:
            res += spell.upper()
        
    return res


if __name__ == "__main__":
    s = input()
    print(func(s))
