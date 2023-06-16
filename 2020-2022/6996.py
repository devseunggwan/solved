from collections import Counter

for _ in range(int(input())):
    A, B = input().split()
    C = ""
    if(Counter(A) != Counter(B)):
        C = " NOT"

    print("{} & {} are{} anagrams.".format(A, B, C))