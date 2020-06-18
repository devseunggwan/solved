ans = ""
for i in input():
    if(i.isupper()): ans += i.lower()
    else: ans += i.upper()
    
print(ans)