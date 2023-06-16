a = [i for i in map(int, input().split())]
if(a[0]%a[1] == 0): print(a[3]*a[2]*((a[0]//a[1])-1))
else:  print(a[3]*a[2]*((a[0]//a[1])))