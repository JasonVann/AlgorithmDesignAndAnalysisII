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
    import copy
    (n, data) = load_data1(is_test)
    data0 = copy.deepcopy(data)
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
            cur = v[0][0]
            q = v[0][1]
            if head[q] == head[k]:
                # Then they are already in the same cluster
                continue
            if min_d == None or min_d > cur:
                min_d = cur
                (p_min, q_min) = (k, v[0][1])
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
    '''
    c_keys = cluster.keys()
    while k < len(c_keys) - 1:
        for v1 in cluster[c_keys[k]]:
            for v2 in cluster[c_keys[k+1]]:
                cur_d = None
                if v1 in data:
                    for a_tuple in data[v1]:
                        if a_tuple[1] == v2:
                            cur_d = a_tuple[0]
                if cur_d == None:
                    for a_tuple in data[v2]:
                        if a_tuple[1] == v1:
                            cur_d = a_tuple[0]
                            
                if min_d == None or min_d > cur_d:
                    min_d = cur_d
                    p_min = v1
                    q_min = v2
        k += 1
    '''
    #print data
    for k, v in data0.items():
        for (w, q) in v:
            if head[k] != head[q]:
                if min_d == None or min_d > w:
                    min_d = w
                    (p_min, q_min) = (k, q)
                
    print 89, min_d, (p_min, q_min)
    return (head, cluster)

(n, data) = load_data1(False)
(head, cluster) = max_k(3, True)
(head, cluster) = max_k(4, False)

print time.time() - start_time
