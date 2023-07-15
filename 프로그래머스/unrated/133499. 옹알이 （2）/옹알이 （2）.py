def solution(babbling):
    answer = 0
    speak_list = ["aya", "ye", "woo", "ma"]
    
    for babb in babbling:
        is_babb_list = [0] * len(babb)
        previous_speak = ""
        
        # 발음하는 문자가 speak_list에 포함되는 경우
        if babb in speak_list:
            answer += 1
            continue
        
        for idx in range(len(babb)):
            for speak in speak_list:
                if len(babb) < idx+len(speak):
                    continue
                
                if speak == babb[idx:idx+len(speak)] and speak != previous_speak:
                    is_babb_list[idx:idx+len(speak)] = [1] * len(speak)
                    previous_speak = speak
            
            # 다른 글자를 보지 않더라도 발음이 가능한 경우
            if all(is_babb_list):
                break
        
        # 발음이 가능한 경우, 정답 + 1
        answer += int(all(is_babb_list))
    
    return answer