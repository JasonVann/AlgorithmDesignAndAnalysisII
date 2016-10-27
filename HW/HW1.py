import time

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

#(n, res) = load_data1()
schedule_job()
print 'Now Q2'
schedule_job(False)

print time.time() - start_time
