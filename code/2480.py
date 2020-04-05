import collections

D = collections.Counter(map(int, input().strip().split()))
if(max(D.values()) == 1):
    print(max(D.keys())*100)
elif(max(D.values()) == 2):
    print(1000 + D.most_common(1)[0][0]*100)
elif(max(D.values()) == 3):
    print(10000 + D.most_common(1)[0][0] * 1000)
