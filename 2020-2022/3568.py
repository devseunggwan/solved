var = input().strip().split()
varType= var[0] 

for i in range(1, len(var)):
    var[i] = var[i][:-1]
    varLoc, varForRev = 0, ""

    for j in range(len(var[i])-1, -1, -1):
        if(var[i][j].isalpha()):
            varLoc = j
            break

    varFor = var[i][varLoc+1:][::-1]
    for j in range(len(varFor)):
        
        if(varFor[j] == ("[")):
            varForRev += "[]"
        elif(varFor[j] == ("]")):
            continue
        else: 
            varForRev += varFor[j] 
    

    print("{}{} {};".format(varType, varForRev, var[i][:varLoc+1]))