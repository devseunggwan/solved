from collections import Counter

def tc1(sentence, tc):
    """
    글자 개수가 두개 이상 넘어가는 경우 판별
    이 경우, 비슷한 단어가 아니다.
    """
    
    return abs(sum(sentence.values()) - sum(tc.values())) > 1

def tc2(sentence, tc):
    """
    두 단어가 같은 구성을 갖는 경우 판별
    """
    
    try:
        # 두 문장이 갖고 있는 스팰링 종류가 같은 지 판별
        if set(sentence) & set(tc) != set(sentence) | set(tc):
            return 0
        # 스팰링 개수가 같은 지 판별
        else:
            for entity in tc:
                if sentence[entity] != tc[entity]:
                    return 0
    except:
        return 0
    
    return 1


def tc3(sentence, tc):
    """
    다른 문자로 바뀌거나, 더해지거나 빼진 경우 판별 
    """
    
    res = 0
    # 하나의 문자를 sentence 내 없는 다른 문자로 바꾼 경우
    if set(sentence) & set(tc) != set(sentence) | set(tc):
        cnt = 0
        
        if len(set(tc) - set(sentence)) > 1:
            return 0
        
        # 여집합 항목들에 대해서 몇개가 바꼈는 지 카운팅
        for spell in tc:
            if not sentence[spell]:
                cnt += tc[spell]
            else:
                cnt += abs(sentence[spell] - tc[spell])
        for spell in sentence:
            if not tc[spell]:
                cnt += sentence[spell]
                
        return 0 if cnt > 2 else 1
        
    # 문장 내에 있는 spell 중에서 바꾼 경우
    else:
        cnt = 0
        for spell in tc:
            # 바꾼 개수를 카운팅함
            cnt += abs(sentence[spell] - tc[spell])
        
        # 하나를 다른 문자로 바꾼 경우(+-): 2
        # 단순하게 추가만 한 경우: 1
        # 단순하게 삭제만 한 경우: 1
        # 순서만 바꾼 경우: 0
        if cnt <= 2:
            return 1
        else:
            return 0 

if __name__ == "__main__":
    N = int(input()) - 1
    sentence = Counter(input())
    answer = 0
    
    for _ in range(N):
        tc = Counter(input())
        
        if (not tc1(sentence, tc)) and (tc2(sentence, tc) or tc3(sentence, tc)):
            answer += 1
            
    print(answer)