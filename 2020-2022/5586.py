S = input()

JOI, IOI = 0, 0

for i in range(len(S)-2):
    if(S[i:i+3] == "JOI"): JOI += 1
    if(S[i:i+3] == "IOI"): IOI += 1

print("{}\n{}".format(JOI, IOI))