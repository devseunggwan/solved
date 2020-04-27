for i in range(101):
    I = i*i*i
    for j in range(2, i):
        J = j*j*j
        for k in range(j, i):
            K = k*k*k
            for l in range(k, i):
                L = l*l*l
                if(I == J+K+L):
                    print("Cube = {}, Triple = ({},{},{})".format(i, j, k, l))
                if(I < J+K+L):
                    break
