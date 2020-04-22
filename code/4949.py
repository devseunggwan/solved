while True:
    test = input()
    check = False
    stack = []
    if(test == "."):
        break
    else:
        for i in test:
            if(i == "["):
                stack.append("[")
            elif(i == "("):
                stack.append("(")
            elif (i == "]"):
                if(len(stack) == 0):
                    check = True
                    break
                elif(stack[-1] != "["):
                    check = True
                    break
                else:
                    stack.pop(-1)
            elif (i == ")"):
                if(len(stack) == 0):
                    check = True
                    break
                elif(stack[-1] != "("):
                    check = True
                    break
                else:
                    stack.pop(-1)
    if(check):
        print("no")
    elif(len(stack) == 0):
        print("yes")
    else:
        print("no")
