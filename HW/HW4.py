import time
import sys
import numpy

start_time = time.time()

def load_data():
    file_name = 'g2.txt'
    #file_name = 'HW4_test3.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    head = lines[0].split('\t')
    if len(head) == 1:
        head = lines[0].split(' ')
    (n, m) = head
    (n, m) = (int(n), int(m))

    data = {}
    for line in lines[1:]:
        if line == '':
            continue
        row = line.split('\t')
        if len(row) == 1:
            row = line.split(' ')
        tail = int(row[0])
        head = int(row[1])
        weight = int(row[2])
        dic2 = {}
        #dic2[head] = weight
        if tail in data:
            #data[tail] = data[tail] + [(tail, weight)]
            data[tail][head] = weight
        else:
            #data[tail] = [(tail, weight)]
            data[tail] = {}
            data[tail][head] = weight
            
    #print (n, m)
    return n, m, data

def floyd_warshall():
    global start_time
    n, m, data = load_data()
    A = []
    '''
    for i in range(n+1):
        row = []
        for j in range(n+1):
            row.append([0] * (n+1))
        A.append(row)
    '''
    # Use numpy to save more RAM
    A = numpy.zeros((n+1, n+1, n+1))
    #print A

    print 55, 'A initialized', time.time() - start_time
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                A[i][j][0] = 0
            elif i in data and j in data[i]:
                A[i][j][0] = data[i][j]
            else:
                A[i][j][0] = sys.maxsize
                #A[i][j][0] = None
    #return A
    print 67, 'A[0] assigned', time.time() - start_time
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                a1 = A[i][j][k-1]
                a2 = A[i][k][k-1]
                a3 = A[k][j][k-1]
                res = min(a1, a2+a3)
                if i == j and res < 0:
                    print 77, i, j, k
                    return 'Negative cycle found!'
                A[i][j][k] = res

    print 80, 'A assigned', time.time() - start_time
    
    min_sp = None
    found_neg = False
    for i in range(1, n+1):
        if A[i][i][n] < 0:
            #print 69, 'found negative cycle!'
            found_neg = True
        for j in range(1, n+1):
            if A[i][j][n-1] == None:
                continue
            if min_sp == None or A[i][j][n-1] < min_sp:
                min_sp = A[i][j][n-1]

    print 94, min_sp, found_neg
    
    return A

n, m, data = load_data()
A = floyd_warshall()

print time.time() - start_time
