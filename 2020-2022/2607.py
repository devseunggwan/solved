from collections import Counter
ans = 0
A = [input() for i in range(int(input()))]
AC = Counter(A[0])
for i in A[1:]:
    if(max(Counter(i).values()) > 2):
        continue
    elif(abs(len(A[0]) - len(i)) >= 2):
        continue
    elif(len(set(Counter(i).keys())) == 1 and len((set(Counter(i).keys())).difference(set(AC.keys()))) == 0):
        ans += 1
        print(i)
    elif(len(set(AC.keys()) - set(Counter(i).keys())) < 2 and max(Counter(i).values()) == 1):
        ans += 1
        print(i)

    elif(AC.keys() == Counter(i).keys()):
        ans += 1
        print(i)


print(ans)
