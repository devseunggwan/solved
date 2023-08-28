N = int(input())
students = [set([i]) for i in range(N)]
grades = [list(map(int, input().split())) for _ in range(N)]

# 각 학년 별로
for i in range(5):
    grade_map = {}
    
    # 학생 별 반을 배정하고
    for idx, g in enumerate(grades):
        if g[i] not in grade_map:
            grade_map[g[i]] = [idx]
        else:
            grade_map[g[i]].append(idx)
    
    for g_key in grade_map.keys():
        # 같은 반이 된 학생들이 있으면 
        if len(grade_map[g_key]) > 1:
            # 각 친구 별 같은 반 된 친구들 리스트에 추가한다.
            for g in grade_map[g_key]:
                for member in grade_map[g_key]:
                    students[g].add(member)    
    
max_duplicated_student = 0
max_duplicated_count = 0
# 가장 많은 친구들과 반이 된 친구를 찾는다.
# 같은 빈도로 친구들과 반이 되었으면 가장 순서가 앞인 번호가 반장이 된다.
for member, friends in enumerate(students):
    if len(friends) > max_duplicated_count:
        max_duplicated_count = len(friends)
        max_duplicated_student = member + 1

print(max_duplicated_student)
