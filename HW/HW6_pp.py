import time
import math
import random
import copy

start_time = time.time()

def load_data():
    file_name = '2SAT1.txt'
    #file_name = 'HW6_test5.txt'
    lines = [line.strip('\r\n') for line in open(file_name)]
    n = int(lines[0])
    data = []
    for line in lines[1:]:
        if line == '':
            continue
        temp = line.split(' ')
        if len(temp) == 1:
            temp = line.split('\t')
        a, b = int(temp[0]), int(temp[1])
        data += [(a,b)]
    return n, data

def papadimitriou():
    n, data0 = load_data()
    print 26, 'data loaded'
    true_dic0 = {}

    n = 10000
    for i in range(1, n+1):
        true_dic0[i] = [True, False]

    print 30, 'dic initialized'

    i_max = math.ceil(math.log(n)) * 1
    for i in range(int(i_max)):
        data = copy.deepcopy(data0)
        true_dic = copy.deepcopy(true_dic0)
        initial = random.randint(1, n)
        true_dic[initial].pop(random.choice(true_dic[initial]))
        true_dic[initial] = true_dic[initial][0]
        for j in range(2*n**2):
            if len(data) == 0:
                return 'Found!'
            temp = random.choice(data)
            new_v = random.choice(temp)
            if new_v > 0:
                if true_dic[new_v] == False:
                    break
                true_dic[new_v] = True
            else:
                if true_dic[-new_v] == True:
                    break
                true_dic[-new_v] = False
            data.remove(temp)

    return 'Unsatisfiable!'

n, data = load_data()
print papadimitriou()

print time.time() - start_time
