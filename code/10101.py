import collections

T = [int(input()) for i in range(3)]
t = collections.Counter(T)

if(sum(T) != 180):
    print("Error")
elif(sum(T) == 180 and len(t.keys()) == 3):
    print("Scalene")
elif(sum(T) == 180 and t.most_common(1)[0][1] == 2):
    print("Isosceles")
elif(sum(T) == 180 and t.most_common(1)[0][1] == 3 and t.most_common(1)[0][0] == 60):
    print("Equilateral")
