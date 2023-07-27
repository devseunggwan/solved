import sys
from collections import Counter
    
sentence = sys.stdin.read().replace(" ", "").replace("\n", "")
c = Counter(sentence)
__max = c.most_common(1)[0][1]

print("".join(sorted([key for key, value in c.items() if value == __max])))