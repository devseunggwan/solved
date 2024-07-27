sentence = input().strip().upper()
answer = 0
for i in range(0, len(sentence), 3):
    chunk = sentence[i:i+3]
    answer += sum([chunk[0] != "P", chunk[1] != "E", chunk[2] != "R"])
    
print(answer)