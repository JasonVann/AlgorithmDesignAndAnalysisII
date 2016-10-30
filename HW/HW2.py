import time

start_time = time.time()

def load_data1(is_test):
    if not is_test:
        file_name = 'clustering1.txt'
    else:
        file_name = 'HW2_test1.txt'
        
    lines = [line.strip('\r\n') for line in open(file_name)]
    #print 58, lines[0]
    n  = int(lines[0])
    #print 59, header

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
    for k, v in res.items():
        v.sort(key = lambda k: (k[0], k[1]), reverse = False)
    return (n,  res)

def max_k(num_k, is_test):
    (n, data) = load_data1(is_test)
    #data0 = copy.deepcopy(data)
    num = num_k
    head = {}
    cluster = {}
    for i in range(1, n+1):
        head[i] = i
        cluster[i] = [i]
    while n > num:
    #while len(connected) > num:
        min_d = None
        (u, v) = (None, None)
        for k, v in data.items():
            i = 0
            while True:
                cur = v[i][0]
                q = v[i][1]
                if head[q] != head[k]:
                    # Then they are not in the same cluster
                    if min_d == None or min_d > cur:
                        min_d = cur
                        (p_min, q_min) = (k, v[i][1])
                    break
                else:
                    i+=1
                    if i == len(v):
                        break
                    
        #print 46, (p_min, q_min), min_d
        p_head = head[p_min]
        q_head = head[q_min]
        if len(cluster[p_head]) > len(cluster[q_head]):
            a, b = p_head, q_head
        else:
            a, b = q_head, p_head

        #if cluster[a] != [-1]:
        cluster[a].extend(cluster[b])
        #else:
        #    cluster[a] = [b]
        for temp in cluster[b]:
            head[temp] = a
        cluster.pop(b)
        
        data[p_min].remove((min_d, q_min))
        
        n -= 1

    min_d = None
    k = 0
    #print data
    for k, v in data.items():
        for (w, q) in v:
            if head[k] != head[q]:
                if min_d == None or min_d > w:
                    min_d = w
                    (p_min, q_min) = (k, q)
    
    print 89, min_d, (p_min, q_min)
    return (head, cluster)

def load_data2(is_test):
    if not is_test:
        file_name = 'clustering_big.txt'
    else:
        file_name = 'HW2_test2.txt'
        
    lines = [line.strip('\r\n') for line in open(file_name)]

    head  = lines[0].split('\t')
    if len(head) == 1:
        head = lines[0].split(' ')

    (n, b) = head
    (n, b) = (int(n), int(b))

    res = {}
    j = 1
    for i in range(1, len(lines)):
        if lines[i] == '':
            continue
        temp = lines[i].split('\t')
        if len(temp) == 1:
            temp = lines[i].split(' ')
        #print 118, temp
        temp = [a for a in temp if a != '']
        #print 120, temp
        temp = ''.join(temp)
        res[j] = temp
        j += 1
        
    return ((n, b),  res)



    
def max_k_big(num_k, is_test):
    def cal_d(p, q):
        res = int(p, 2) ^ int(q, 2)
        d = bin(res).count('1')
        return d
            
    ((n, b),  data) = load_data2(is_test)
    #data0 = copy.deepcopy(data)
    num = num_k
    n0 = n
    head = {}
    cluster = {}
    for i in range(1, n+1):
        head[i] = i
        cluster[i] = [i]
    while n > num:
        #while len(connected) > num:
        min_d = None

        for i in range(1, n0+1):
            for j in range(i+1, n0+1):

                if head[i] == head[j]:
                    continue

                d = cal_d(data[i], data[j])       
                if min_d == None or min_d > d:
                    min_d = d
                    (p_min, q_min) = (i, j)
                    #break
        #print 157, head
        #print 158, (p_min, q_min), min_d, d, head[p_min], head[q_min]
        p_head = head[p_min]
        q_head = head[q_min]
        if len(cluster[p_head]) > len(cluster[q_head]):
            a, b = p_head, q_head
        else:
            a, b = q_head, p_head

        #print 166, cluster[a], cluster[b], a, b
        #if cluster[a] != [-1]:
        cluster[a].extend(cluster[b])
        #else:
        #    cluster[a] = [b]
        for temp in cluster[b]:
            head[temp] = a
        cluster.pop(b)
        #print 174, cluster[a], a, b
        '''
        if min_d >= 3:
            break
        '''
        n -= 1

    min_d = None
    k = 0
    #print data
    for i in range(1, n0+1):
        for j in range(i+1, n0+1):
            if head[i] != head[j]:
                d = cal_d(data[i], data[j])
                if min_d == None or min_d > d:
                    min_d = d
                    (p_min, q_min) = (i, j)
    
    print 186, min_d, (p_min, q_min)
    return (head, cluster)


#(n, data) = load_data1(False)
#(head, cluster) = max_k(3, True)
#(head, cluster) = max_k(4, False)

#((n, b), data) = load_data2(False)
(head, cluster) = max_k_big(3, True)
#(head, cluster) = max_k_big(2, False)

print time.time() - start_time
