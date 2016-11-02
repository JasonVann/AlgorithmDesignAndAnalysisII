def optimal_bst(pl):
    A = []
    n = len(pl)
    for i in range(n):
        A.append([0]*(n))
        
    for s in range(0, n):
        for i in range(0, n-s):
        #for i in range(n-s, 0, -1):
            temp = None
            for k in range(i, i+s+1):
                #print 9, A, s, i, k
                if i > k - 1:
                    t2 = 0
                else:
                    t2 = A[i][k-1]
                if k + 1 > i + s:
                    t3 = 0
                else:
                    t3 = A[k+1][i+s]
                t1 = sum(pl[i:i+s+1])
                #print 19, t1, t2, t3, temp
                cur = t1 + t2 + t3
                if temp == None or cur < temp:
                    temp = cur
            #print 23, temp
            #Ai.append(temp)
            #print 29, i, s
            A[i][i+s] = temp
           
        #A.append(Ai)
        
    print A
    return A[0][n-1]
    
pl = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
print optimal_bst(pl)
