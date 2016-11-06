import time
import numpy as np
import sys
import math

start_time = time.time()

def load_data():
    file_name = 'tsp.txt'
    file_name = 'HW5_test2.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    n = int(lines[0])
    data = []
    for line in lines[1:]:
        if line == '':
            continue
        temp = line.split('\t')
        if len(temp) == 1:
            temp = line.split(' ')
        row = (float(temp[0]), float(temp[1]))
        data.append(row)
    return n, data

def subset(n):
    nums = []
    for i in range(1, n+1):
        nums.append(i)
    res = [[]]
    for i in nums:
        temp = res[:]
        temp = [a+[i] for a in temp]
        temp = [a for a in temp if 1 in a]
        res.extend(temp)
    data = {}
    #print res
    for i in res:
        n = len(i)
        if n in data:
            data[n] += [i]
        else:
            data[n] = [i]
    data.pop(0)
    return data

def dis(a, b):
    (a1, a2) = a
    (b1, b2) = b
    d = math.sqrt((a1-b1)**2 + (a2-b2)**2)
    return d

def tsp():
    n, data = load_data()
    S = subset(n)
    N = 0
    for key, set in S.items():
        
        for i in range(len(set)):
            set[i] = (N + i, set[i])
        N += len(set)
    print 50, N

    #return S
    A = np.zeros((N, n))

    
    for i in range(1, N):
        A[i][0] = sys.maxsize

    
    for m in range(1, n):
        for idx, s in S[m+1]:
        #for s in S:
            
            for j in s:
                if j == 1:
                    continue
                
                min_v = None
                for idx0, set2 in S[m]:
                    if j in set2:
                        continue
                    for k in s:
                        if k == j:
                            continue
                        cur_dis = A[idx0][k-1] + dis(data[k-1], data[j-1])
                        if min_v == None or min_v > cur_dis:
                            min_v = cur_dis
                A[idx][j-1] = min_v
                    
            #pass

    min_v2 = None
    for j in range(1, n):
        cur_d = A[-1][j] + dis(data[j], data[0])
        if min_v2 == None or min_v2 > cur_d:
            min_v2 = cur_d
            
    print 97, min_v2
    
    return A

n, data = load_data()
A = tsp()
#res = subset(24)


print time.time() - start_time
