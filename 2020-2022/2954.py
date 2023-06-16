M = ['a','e','i','o','u']
ans, plug = "", 0

for i in input().strip():
    if(plug > 0): plug -= 1
    elif(i in M): 
        ans += i
        plug += 2
    else: ans += i

print(ans)