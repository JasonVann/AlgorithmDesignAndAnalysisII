import time

start_time = time.time()

def load_data():
    file_name = 'knapsack1.txt'
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
    print 30, V, n
    A = []
    for i in range(n+1):
        A.append([0])
        
    A[0] += [0] * V
    #print 36, V+1,  A[0][V+1]

    #print 39, data
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
    
#((v, n), data) = load_data()

A = knapsack()

print time.time() - start_time
    
