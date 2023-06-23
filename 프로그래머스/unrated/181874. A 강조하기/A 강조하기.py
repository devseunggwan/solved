def convert(spell):
    return spell.upper() if spell in ["A", "a"] else spell.lower()

def solution(myString):
    return ''.join(map(lambda x: convert(x), list(myString)))