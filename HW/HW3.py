import time

start_time = time.time()

def load_data():
    file_name = 'knapsack_big.txt'
    #file_name = 'HW3_test1.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    head = lines[0].split('\t')
    if len(head) == 1:
        head = lines[0].split(' ')
    V = int(head[0])
    n = int(head[1])

    data = {}
    for i in range(1, len(lines)):
        
        if lines[i] == '':
            continue
        temp = lines[i].split('\t')
        if len(temp) == 1:
            temp = lines[i].split(' ')
        data[i] = (int(temp[0]), int(temp[1])) #v, w

    print 24, len(lines)
    return ((V, n), data)

def knapsack():
    ((V, n), data) = load_data()
    #res = {}
    print 40, V, n
    A = []
    n = 40 #2.5G for 100
    for i in range(n+1):
        A.append([0])
    
    A[0] += [0] * V
    #print 36, V+1,  A[0][V+1]

    #print 39, data
    #return data
    #return A
    for i in range(1, n+1):
        for x in range(1, V+1):
            (v, w) = data[i]

            if x < w:
                #print 41, i, x
                cur = A[i-1][x]
            else:
                cur = max(A[i-1][x], A[i-1][x - w] + v)
                
            A[i].append(cur)

    #return A
    
    return A[-1][-1]

def knapsack_big2():
    # 25min, 4243395
    ((V, n), data) = load_data()
    #res = {}
    print 30, V, n
    A = []
    #n = 40 #2.5G for 100
    for i in range(1):
        A.append(0)
    A_old = []
    #A_old.append(0)
    
    A_old += [0] * (V+1)
    #print 36, V+1,  A[0][V+1]

    #print 39, data
    #return data
    #return A
    #print A_old
    #print 77, A
    for i in range(1, n+1):
        A = [0]
        for x in range(1, V+1):
            (v, w) = data[i]

            if x < w:
                #print 41, i, x
                cur = A_old[x]
            else:
                #print 86, x, v, w, A_old
                cur = max(A_old[x], A_old[x - w] + v)
                
            A.append(cur)
        #print 90, A, cur
        A_old = A[:]
        #A = [0] * (V+1)
        
        #print 92, A_old

    #print 96, A_old
    #print 97, A
    
    #return A
    
    return A[-1]

def knapsack_big():
    # dictionary, slow, more RAM usage
    ((V, n), data) = load_data()
    #res = {}
    print 30, V, n
    A = []
    n = 50 # 7G!!
    for i in range(n+1):
        dic = {}
        dic[0] = 0
        A.append(dic)

    dic2 = {}
    for i in range(V+1):
        dic2[i] = 0
        
    A[0] = dic2
    
    #print 36, V+1,  A[0][V+1]
    
    #print 39, data
    #return A
    max_del = 1e6
    i, x = 1, 1
    while i < n + 1:
        while x < V + 1:
        #for x in range(1, V+1):
            (v, w) = data[i]

            if x < w:
                #print 41, i, x
                cur = A[i-1][x]
            else:
                cur = max(A[i-1][x], A[i-1][x - w] + v)
                
            A[i][x] = cur
            x += 1
        i += 1
        
    #return A
    
    return A[n][V]

'''
((v, n), data) = load_data()

max_v = 0
max_w = 0
for k, (v, w) in data.items():
    if w > max_w:
        max_w = w
    if v > max_v:
        max_v = v
print max_v, max_w
'''

#A = knapsack()
A = knapsack_big2()

print time.time() - start_time
    
