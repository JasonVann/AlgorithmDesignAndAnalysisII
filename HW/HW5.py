import time
import numpy as np
import sys
import math

start_time = time.time()

def load_data():
    file_name = 'tsp.txt'
    #file_name = 'HW5_test2.txt'
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
    #n = 15
    S = subset(n)
    N = 0
    dic_s_i = {}
    for key, set0 in S.items():
        for i in range(len(set0)):
            dic_s_i[tuple(set0[i])] = N + i
            set0[i] = (N + i, set0[i])

            #print set0, a_tuple

        N += len(set0)
    print 50, N
    
    #print 64, dic_s_i
    
    #return S
    A = np.zeros((N, n))
    
    for i in range(1, N):
        A[i][0] = sys.maxsize

    print 68, 'A initialized'
    #return A
    for m in range(2, n+1):
        for idx, set1 in S[m]:
        #for s in S:
            
            for j in set1:
                if j == 1:
                    continue
                
                min_v = None
                set2 = set1[:]
                set2.remove(j)
                idx0 = dic_s_i[tuple(set2)]
                
                #for idx0, set2 in S[m-1]:
                if True:
                    '''
                    if set(set2 + [j]) != set(set1):
                        continue
                    '''
                    for k in set1:
                        if k == j:
                            continue
                        cur_dis = A[idx0][k-1] + dis(data[k-1], data[j-1])
                        if min_v == None or min_v > cur_dis:
                            min_v = cur_dis
                A[idx][j-1] = min_v
                    
            #pass

    print 96, 'now find the min_v2'

    min_v2 = None
    for j in range(1, n):
        cur_d = A[-1][j] + dis(data[j], data[0])
        if min_v2 == None or min_v2 > cur_d:
            min_v2 = cur_d
            
    print 97, min_v2
    
    return S, A

n, data = load_data()
S, A = tsp()
#res = subset(24)


print time.time() - start_time
