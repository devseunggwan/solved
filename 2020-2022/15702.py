N, M = map(int, input().strip().split())

score = list(map(int, input().strip().split()))
bestExamScore = [100001, 0]

for i in range(M):
    exam = input().strip().split()
    examScore = 0
    for j in range(1, N+1):
        if(exam[j] == "O"):
            examScore += score[j-1]
    
    if((examScore == bestExamScore[1] and int(exam[0]) < bestExamScore[0]) or examScore > bestExamScore[1]):
        bestExamScore = [int(exam[0]), examScore]
    
print(*bestExamScore)