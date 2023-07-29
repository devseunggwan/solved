from typing import List

def split_polynomio(polynomio: str) -> List:
    res: List = []
    stack: str = ""
    before: str = ""
    
    for p in polynomio:
        if p != before:
            res.append(stack)
            before, stack = p, p
        else:
            stack += p

    res.append(stack)
    res = res[1:]
    
    return res

def parse_polynomio(polynomio) -> str:
    res: str = ""
    
    for p in polynomio:
        if p[0] == ".":
            res += p
        elif p[0] == "X":
            if len(p) % 2 == 1:
                res = "-1"
                break
            else:
                res += ("AAAA" * (len(p) // 4)) + ("BB" * ((len(p) // 2) % 2))

    return res
    
if __name__ == "__main__":
    polynomio = input()
    polynomio = split_polynomio(polynomio)
    polynomio = parse_polynomio(polynomio)
    print(polynomio)