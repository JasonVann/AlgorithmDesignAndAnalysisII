import time

start_time = time.time()


def load_data1(is_test):
    if not is_test:
        file_name = 'clustering1.txt'
    else:
        file_name = 'HW2_test1.txt'

    lines = [line.strip('\r\n') for line in open(file_name)]
    # print 58, lines[0]
    n = int(lines[0])
    # print 59, header

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
        v.sort(key=lambda k: (k[0], k[1]), reverse=False)
    return (n, res)


def max_k(num_k, is_test):
    (n, data) = load_data1(is_test)
    # data0 = copy.deepcopy(data)
    num = num_k
    head = {}
    cluster = {}
    for i in range(1, n + 1):
        head[i] = i
        cluster[i] = [i]
    while n > num:
        # while len(connected) > num:
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
                    i += 1
                    if i == len(v):
                        break

        # print 46, (p_min, q_min), min_d
        p_head = head[p_min]
        q_head = head[q_min]
        if len(cluster[p_head]) > len(cluster[q_head]):
            a, b = p_head, q_head
        else:
            a, b = q_head, p_head

        # if cluster[a] != [-1]:
        cluster[a].extend(cluster[b])
        # else:
        #    cluster[a] = [b]
        for temp in cluster[b]:
            head[temp] = a
        cluster.pop(b)

        data[p_min].remove((min_d, q_min))

        n -= 1

    min_d = None
    k = 0
    # print data
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
        file_name = 'HW2_test24.txt'

    lines = [line.strip('\r\n') for line in open(file_name)]

    head = lines[0].split('\t')
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
        # print 118, temp
        temp = [a for a in temp if a != '']
        # print 120, temp
        temp = ''.join(temp)
        res[j] = temp
        j += 1

        '''
        if i > 100:
            break
        '''
    return ((n, b), res)


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
        # return head


def build_close_bit(data):
    close = {}

    inv_data = {}
    count = 0
    for k, v in data.items():
        inv_data[v] = k

    for k, v in data.items():
        temp = []
        # 1 bit off
        if v in inv_data and inv_data[v] != k:
            temp.append((v))

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
    ((n, b), data) = load_data2(is_test)
    # data0 = copy.deepcopy(data)

    # n = 1000

    print 219, 'Data loaded', n

    list_data = []
    for k, v in data.items():
        list_data.append((k, v))

    (close, inv_data) = build_close_bit(data)

    last_count = 0
    for i in close:
        last_count += len(close[i])
    print 202, 'initial count: ', last_count

    # print list_data
    num = num_k
    n0 = n
    head = {}
    cluster = {}
    exe_count = 0

    for i in range(1, n + 1):
        head[i] = (i, 0)  # rank 0
        # cluster[i] = [i]

    found = False

    # for i in range(1, n0+1):
    #    for j in range(i+1, n0+1):
    for l1 in range(0, len(data)):
        idx1 = l1 + 1
        if len(close[idx1]) == 0:
            l1 += 1
            continue

        for v in close[idx1]:
            found = True
            idx2 = inv_data[v]
            union(idx1, idx2, head)

    # print 157, head
    # print 158, (p_min, q_min), min_d, d, head[p_min], head[q_min]

    print 211, n

    list_heads = set()
    for k, v in head.items():
        (a, b) = v
        if a == k:
            list_heads.add(a)

    set_heads = set()
    for x in data:
        x_head = find(x, head)
        set_heads.add(x_head)

    print 336, '# of groups: ', len(list_heads), len(set_heads)

    return (head, cluster)

# (n, data) = load_data1(False)
# (head, cluster) = max_k(3, True)
# (head, cluster) = max_k(4, False)

# ((n, b), data) = load_data2(True)
#(head, cluster) = max_k_big(2, True)
(head, cluster) = max_k_big(2, False)

print time.time() - start_time
