for i in range(int(input())):
    stack = []
    for i in input():
        if(i == "("):
            stack.append("(")
        elif(i == ")" and len(stack) == 0):
            stack = ["error"]
            break
        else:
            stack.pop(-1)

    if(len(stack) == 0):
        print("YES")
    else:
        print("NO")
