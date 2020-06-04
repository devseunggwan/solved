N = int(input())
ans = 0
L = [9, 90 * 2, 900 * 3, 9000 * 4, 90000 * 5, 900000 * 6, 9000000 * 7, 90000000 * 8]
if(N < 10): print(N)
else:
    ans += sum(L[:len(str(N))-1]) + (len(str(N)) * (N - (10 ** (len(str(N))-1)) + 1))
    print(ans)