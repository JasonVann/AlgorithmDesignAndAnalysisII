import time
import random

start_time = time.time()

def load_data1():
    file_name = 'jobs.txt'
    #file_name = 'HW1_test1.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    n = lines[0]
    res = []
    for i in range(1, len(lines)):
        if lines[i] == '':
            continue
        
        temp = lines[i].split('\t')
        
        if len(temp) == 1:
            temp = lines[i].split(' ')
        
        temp = [int(a) for a in temp]
        res.append(temp)
    return (n, res)

def schedule_job(by_diff = True):
    (n, data) = load_data1()
    
    for a in data:
        if by_diff:
            a.insert(0, a[0] - a[1])
        else:
            a.insert(0, a[0]*1.0/a[1])

    data.sort(key = lambda k: (k[0], k[1]), reverse = True)
    #print data[:10]

    total = 0
    cumu_data = []
    cumu = 0
    for a in data:
        cumu += a[2]
        cumu_data.append([a[0], a[1], cumu])
    
    times = [a[1]*a[2] for a in cumu_data]
    total = sum(times)
    '''
    print 35, data
    print 42, cumu_data
    print 43, times
    '''
    print total
    
    #total = reduce(lambda: a:

def load_data3():
    file_name = 'edges.txt'
    file_name = 'HW1_test3.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    #print 58, lines[0]
    header  = lines[0].split('\t')
    #print 59, header
    if len(header) == 1:
        header = lines[0].split(' ')
    (n, m) = (int(header[0]), int(header[1]))
    
    res = {}
    for i in range(1, len(lines)):
        if lines[i] == '':
            continue
        temp = lines[i].split('\t')
        if len(temp) == 1:
            temp = lines[i].split(' ')
        temp = [int(a) for a in temp]
        if temp[0] in res:
            res[temp[0]] += [(temp[2], temp[1])]
        else:
            res[temp[0]] = [(temp[2], temp[1])]

    return ((n,m),  res)

def mst():
    ((n, m), data) = load_data3()
    # n: # of nodes
    V = data.keys()
    X = []
    initial = random.choice(V)
    #initial = 63
    X.append(initial)
    V.remove(initial)
    
    for temp in range(1, n+1):
        if temp not in data:
            data[temp] = []
            V.append(temp)
    
    T = []
    for k, v in data.items():
        v = v.sort()

    #return data
    #print 98, data
    #print 99, V
    #print 100, X, V
    total_score = 0
    while len(V) > 0:
        score = None
        selected_u = None
        selected_v = None
        #for u in X:
        for u in data:
            u_score = None
            for a in data[u]:
                (w, v) = a
                #print 110, a, V, X, u
                if (u in X and v in V) or (u in V and v in X):
                    u_score = w
                    #print 113, (w,v), u_score
                    if score == None or u_score < score:
                        score = u_score
                        if v in V:
                            selected_u = u
                            selected_v = v
                        else:
                            selected_u = v
                            selected_v = u
                        #print 113, u, v
                        break
        #print 117, X, selected_u, selected_v
        #print 118, V, total_score, score
        X.append(selected_v)
        #print 111, X, selected_v, u, v
        V.remove(selected_v)
        total_score += score
        #break
    
    print len(X), len(V), total_score
    
#(n, res) = load_data1()
schedule_job()
print 'Now Q2'
schedule_job(False)

#((n, m),data) = load_data3()

data = mst()

print time.time() - start_time
