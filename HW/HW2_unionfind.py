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
        file_name = 'HW2_test23.txt'
                
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

        '''
        if i > 100:
            break
        '''
    return ((n, b),  res)

def cal_d(p, q):
    res = int(p, 2) ^ int(q, 2)
    d = bin(res).count('1')
    return d

def find(x, head):
    (h, r) = head[x]
    if h != x:
        h_new = find(h, head)
        head[x] = (h_new, r)
    return head[x][0]

def union(x, y, head):
    x_head = find(x, head)
    y_head = find(y, head)
    if x_head == y_head:
        return
    (xh, xr) = head[x]
    (yh, yr) = head[y]
    if xr < yr:
        (x1, r1) = head[xh]
        head[xh] = (yh, xr)
    elif xr > yr:
        (y1, r2) = head[yh]
        head[yh] = (xh, r2)
    else:
        (y1, r2) = head[yh]
        head[yh] = (xh, r2)
        xr = xr + 1
        head[x] = (xh, xr)
    #return head


def build_close_bit(data):
    close = {}

    inv_data = {}
    count = 0
    for k, v in data.items():
        inv_data[v] = k

    for k, v in data.items():
        temp = []
        # 1 bit off
        for i in range(len(v)):
            cur = list(v)
            if v[i] == '1':
                cur[i] = '0'
            else:
                cur[i] = '1'
            # print 143, v, cur
            cur = ''.join(cur)
            if cur in inv_data:
                count += 1
                temp.append(''.join(cur))

        # 2 bits off
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                cur = list(v)
                if v[i] == '1':
                    cur[i] = '0'
                else:
                    cur[i] = '1'
                if v[j] == '1':
                    cur[j] = '0'
                else:
                    cur[j] = '1'
                # print 158, v, cur
                cur = ''.join(cur)
                if cur in inv_data:
                    count += 1
                    temp.append(''.join(cur))
        close[k] = temp
    print '173 count', count
    return (close, inv_data)


data = {}
data[1] = '0110'
data[2] = '1010'


# ((n, b), data) = load_data2(True)
# (close, inv_data) = build_close_bit(data)
# return

def max_k_big(num_k, is_test):
    # Too slow
    ((n, b),  data) = load_data2(is_test)
    #data0 = copy.deepcopy(data)

    #n = 1000

    print 219, 'Data loaded', n

    '''
    for i in range(n, n+1):
        data.pop(i)
    '''

    list_data = []
    for k, v in data.items():
        list_data.append((k, v))

    '''
    (close, inv_data) = build_close_bit(data)
    import copy
    # close2 = copy.deepcopy(close)
    list_data = []
    for k, v in data.items():
        list_data.append((k, v))


    last_count = 0
    for i in close:
        last_count += len(close[i])
    print 202, 'initial count: ', last_count
    '''

    list_data.sort(key = lambda(k): (k[1].count('1'), k[0]))
    #return list_data
    #print list_data
    num = num_k
    n0 = n
    head = {}
    cluster = {}
    print 147, n, len(list_data)
    exe_count = 0
    
    for i in range(1, n+1):
        head[i] = (i, 0) # rank 0
        #cluster[i] = [i]
    while n > num:
        #while len(connected) > num:
        min_d = None
        found = False

        #for i in range(1, n0+1):
        #    for j in range(i+1, n0+1):
        for l1  in range(0, len(list_data)):
            if found:
                break
            for l2 in range(l1+1, len(list_data)):
                exe_count += 1
                (i, b1) = list_data[l1]
                (j, b2) = list_data[l2]
                #print 160, l1, l2, b1, b2
                if abs(b1.count('1') - b2.count('1')) >= 3:
                    break

                #print 166, head[i], head[j], i, j
                if find(i, head) == find(j, head):
                    continue
                
                d = cal_d(data[i], data[j])
                #print 167, i, j, d
                if min_d == None or min_d > d:
                    min_d = d
                    (p_min, q_min) = (i, j)
                    #break

                if d < 3:
                    found = True
                    break
        #print 157, head
        #print 158, (p_min, q_min), min_d, d, head[p_min], head[q_min]

        if not found:
            print 286, 'Cannot find any close pairs'
            break

        p_head = find(p_min, head)
        (p_head, p_rank) = head[p_min]
        q_head = find(q_min, head)
        (q_head, q_rank) = head[q_min]

        union(p_min, q_min, head)

        #(p_head, p_rank) = head[p_min]
        #(q_head, q_rank)  = head[q_min]
        #print 178, p_head, q_head, p_min, q_min
        #print 179, head[p_head], head[q_head]
        #if head[p_head][1] > head[q_head][1]:
        '''
        if p_rank > q_rank:
            a, b = p_head, q_head
        else:
            a, b = q_head, p_head
        
        #print 166, cluster[a], cluster[b], a, b
        #if cluster[a] != [-1]:
        #cluster[a].extend(cluster[b])
        #else:
        #    cluster[a] = [b]
        
        if head[a][1] == head[b][1]:
            #print 193, head[a]
            (h, r) = head[a]
            head[a] = (h, r+1)
        #for temp in cluster[b]:
        for temp in data:
            (h, r) = head[temp]
            if h == b:
                head[temp] = (a, r)
        #cluster.pop(b)
        #print 174, cluster[a], a, b
        '''
        #union(p_min, q_min, head)
        
        if min_d >= 3:
            break
        
        n -= 1

    print 211, n
    min_d = None
    k = 0
    #print n0, data
    for i in range(1, n0+1):
        for j in range(i+1, n0+1):
            exe_count += 1
            if head[i][0] != head[j][0]:
                d = cal_d(data[i], data[j])
                if min_d == None or min_d > d:
                    min_d = d
                    (p_min, q_min) = (i, j)

    print 264, exe_count, 'n=', n
    print 186, min_d, (p_min, q_min)
    return (head, cluster)


#(n, data) = load_data1(False)
#(head, cluster) = max_k(3, True)
#(head, cluster) = max_k(4, False)

#((n, b), data) = load_data2(True)
#(head, cluster) = max_k_big(2, True)
(head, cluster) = max_k_big(2, False)

print time.time() - start_time
