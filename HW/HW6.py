import time
import math
import random
import copy

start_time = time.time()

def load_data():
    file_name = '2SAT6.txt'
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
        #print 20, temp, temp[0]
        a, b = int(temp[0]), int(temp[1])
        data += [(a,b)]
    return n, data

def verify(true_dic, data):
    unmet_data = []
    for (a, b) in data:
        bool_a = False
        bool_b = False
        if (a < 0 and true_dic[-a] == False) or (a > 0 and true_dic[a] == True):
            bool_a = True
        if (b < 0 and true_dic[-b] == False) or (b > 0 and true_dic[b] == True):
            bool_b = True
        if (not bool_a) and (not bool_b):
            #return False
            unmet_data += [(a, b)]
    return unmet_data

def reduce_clause(data):
    dic = {}
    found = True   
    true_set = set()
    false_set = set()
    N = len(data)
    while found:
        found = False        
        failed_set = set()
        
        for i in range(len(data)):
            if data[i] == None:
                continue
            (a, b) = data[i]
            if a > 0:
                if a not in false_set and a not in failed_set:
                    true_set.add(a)
                elif a in false_set:
                    failed_set.add(abs(a))
                    false_set.remove(abs(a))                    
            else:
                if abs(a) in true_set:
                    failed_set.add(abs(a))
                    true_set.remove(abs(a))
                else:
                    if abs(a) not in failed_set:
                        false_set.add(abs(a))
            if b > 0:
                if b not in false_set and b not in failed_set:
                    true_set.add(b)                
                elif b in false_set:
                    failed_set.add(abs(b))
                    false_set.remove(abs(b))
            else:
                if abs(b) in true_set:
                    failed_set.add(abs(b))
                    true_set.remove(abs(b))
                else:
                    if abs(b) not in failed_set:
                        false_set.add(abs(b))
                
        for i in range(len(data)):
            if data[i] == None:
                continue
            (a, b) = data[i]
            if abs(a) not in failed_set:
                data[i] = None
                found = True
                continue
            if abs(b) not in failed_set:
                data[i] = None
                found = True
    
    #print 124, data
    #print 125, true_set, false_set, failed_set
    
    data2 = [a for a in data if a != None]
    if len(data2) == 0:
        print 78, 'Success!'
    print 130, len(data), len(data2), len(failed_set)
    return data2
    
n, data = load_data()
#dic = reduce_clause(data)
     
def papadimitriou():
    n, data0 = load_data()
    print 26, 'data loaded'
    true_dic0 = {}

    data0 = reduce_clause(data0)
    n = len(data0)
    if n == 0:
        return '162, Success!'
        
    for (a, b) in data0:
        true_dic0[abs(a)] = [True, False]
        true_dic0[abs(b)] = [True, False]
        
    #data0 = data0[:n]
    print 30, 'dic initialized'

    i_max = math.ceil(math.log(n)) * 1
    for i in range(int(i_max)):
        unmet_data = copy.deepcopy(data0)
        true_dic = copy.deepcopy(true_dic0)
        initial = random.choice(true_dic0.keys())
        true_dic[initial].pop(random.choice(true_dic[initial]))
        true_dic[initial] = true_dic[initial][0]
        #for j in range(2*n**2):
        j_max = 2*n**2
        j = 0
        met_data = {}
        while j < j_max:
            if len(unmet_data) == 0:
                unmet_data = verify(true_dic, data0)
                if len(unmet_data) == 0:
                    return 'Found!'

            #data = copy.deepcopy(data0)

            temp = random.choice(unmet_data)
            a, b = temp
            bool_a = False
            bool_b = False
            if (a < 0 and true_dic[-a] == False) or (a > 0 and true_dic[a] == True):
                bool_a = True
            if (b < 0 and true_dic[-b] == False) or (b > 0 and true_dic[b] == True):
                bool_b = True
            if not (bool_a or bool_b):

            #else:
                new_v = random.choice(temp)

                if new_v > 0:
                    true_dic[new_v] = True
                else:
                    true_dic[-new_v] = False

                if new_v in met_data:
                    old_clause = met_data[new_v]
                    unmet_data += old_clause
                    met_data[new_v] = [temp]
                else:
                    met_data[new_v] = [temp]
            unmet_data.remove(temp)
            j += 1
    return 'Unsatisfiable!'
    
def papadimitriou0():
    # no usage of reduce func
    n, data0 = load_data()
    print 26, 'data loaded'
    true_dic0 = {}

    #n = len(data0)
    #n = 10000
    for i in range(1, n+1):
        true_dic0[i] = [True, False]

    #data0 = data0[:n]
    print 30, 'dic initialized'

    i_max = math.ceil(math.log(n)) * 1
    for i in range(int(i_max)):
        unmet_data = copy.deepcopy(data0)
        true_dic = copy.deepcopy(true_dic0)
        initial = random.randint(1, n)
        true_dic[initial].pop(random.choice(true_dic[initial]))
        true_dic[initial] = true_dic[initial][0]
        #for j in range(2*n**2):
        j_max = 2*n**2
        j = 0
        met_data = {}
        while j < j_max:
            if len(unmet_data) == 0:
                unmet_data = verify(true_dic, data0)
                if len(unmet_data) == 0:
                    return 'Found!'

            #data = copy.deepcopy(data0)

            temp = random.choice(unmet_data)
            a, b = temp
            bool_a = False
            bool_b = False
            if (a < 0 and true_dic[-a] == False) or (a > 0 and true_dic[a] == True):
                bool_a = True
            if (b < 0 and true_dic[-b] == False) or (b > 0 and true_dic[b] == True):
                bool_b = True
            if not (bool_a or bool_b):

            #else:
                new_v = random.choice(temp)

                if new_v > 0:
                    true_dic[new_v] = True
                else:
                    true_dic[-new_v] = False

                if new_v in met_data:
                    old_clause = met_data[new_v]
                    unmet_data += old_clause
                    met_data[new_v] = [temp]
                else:
                    met_data[new_v] = [temp]
            unmet_data.remove(temp)
            j += 1
    return 'Unsatisfiable!'

n, data = load_data()
print papadimitriou()

print time.time() - start_time
