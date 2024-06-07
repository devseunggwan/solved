def solution(friends, gifts):
    answer = 0
    
    gift_map = {friend: {} for friend in friends} # 선물을 누가 누구에게 줬는 지 기록
    gift_points = {friend: 0 for friend in friends} # 선물 포인트를 집계하여 기록
    gift_next_month = {friend: 0 for friend in friends} # 다음달에 선물을 받을 사람 기록
    
    # 주고 받은 선물에 대한 map을 생성합니다.
    gifts = [gift.split() for gift in gifts]
    for gift in gifts:
        __to, __from = gift
        
        if __from not in gift_map[__to]:
            gift_map[__to][__from] = 1
        else:
            gift_map[__to][__from] += 1
    
    # 주고 받은 선물을 표로 나타냅니다.
    for to_friend in friends:
        to_point = sum(gift_map[to_friend].values())
        from_point = sum([gift_map[from_friend].get(to_friend, 0) for from_friend in friends])
        
        gift_points[to_friend] = to_point - from_point
        # print(to_friend, to_point, from_point, gift_points[to_friend])
    
    for i in range(len(friends)): # to_friend
        for j in range(i, len(friends)): # from_friend
            if friends[i] == friends[j]:
                continue
            
            to_gift_point = gift_map[friends[i]].get(friends[j], 0)
            from_gift_point = gift_map[friends[j]].get(friends[i], 0)
            
            # print(friends[i], friends[j], to_gift_point, from_gift_point, gift_points[friends[i]], gift_points[friends[j]])
            
            if to_gift_point == from_gift_point:
                if gift_points[friends[i]] > gift_points[friends[j]]:
                    gift_next_month[friends[i]] += 1
                elif gift_points[friends[i]] < gift_points[friends[j]]:
                    gift_next_month[friends[j]] += 1
            elif to_gift_point < from_gift_point:
                gift_next_month[friends[j]] += 1
            else:
                gift_next_month[friends[i]] += 1
    
    # print(gift_map)
    # print(gift_next_month)
    answer = max(gift_next_month.values())
    
    return answer