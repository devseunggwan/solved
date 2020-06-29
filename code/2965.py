a, b, c = map(int, input().strip().split())
print(max(b-a, c-b)-1)