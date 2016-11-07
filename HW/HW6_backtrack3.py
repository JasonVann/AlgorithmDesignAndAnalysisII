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

def backtrack():
    from collections import deque
    import copy
    
    n, data0 = load_data()
    print 26, 'data loaded'
    true_dic0 = {}
    for i in range(1, n+1):
        #true_dic0[i] = [True, False]
        true_dic0[i] = []
        
    #data0 = data0[:n]
    print 30, 'dic initialized'
    stack = deque()
    #for i in range(len(data0)):
    i = 0
    has_backed = False
    test_started = False
    test1_win = True
    while i < len(data0):
        clause = data0[i]
        (a, b) = clause
        if test_started:
        #if False:
            bool_a1 = False
            bool_b1 = False
            if (a > 0 and true_dic1[a] == True) or (a < 0 and true_dic1[-a] == False):
                bool_a1 = True
            if (b > 0 and true_dic1[b] == True) or (b < 0 and true_dic1[-b] == False):
                bool_b1 = True
            if bool_a1 or bool_b1:
                alter_OK = True
            else:
                if true_dic1[abs(a)] == []:
                    if true_dic1[abs(b)] == []:
                        test1_win = True
                        true_dic0 = true_dic1
                        test_started = False
                    else:
                        true_dic1[abs(a)] = a > 0
                else:
                    true_dic1[abs(b)] = b > 0
                    
        bool_a = False
        bool_b = False
        if (a > 0 and true_dic0[a] == True) or (a < 0 and true_dic0[-a] == False):
            bool_a = True
        if (b > 0 and true_dic0[b] == True) or (b < 0 and true_dic0[-b] == False):
            bool_b = True
        if bool_a or bool_b:
            i += 1
            continue
        # Then the clause is false. 
        if true_dic0[abs(a)] == []:
            # Default to 1st
            if true_dic0[abs(b)] == []:
                stack.append((clause, i, a))
                has_backed = False
                test_started = True
                true_dic1 = copy.deepcopy(true_dic0)
                true_dic1[abs(b)] = b > 0
                
                test1_win = False
                true_dic0[abs(a)] = a > 0
                i += 1
                continue
            else:
                a, b = b, a
        if true_dic0[abs(b)] == []:
            # a is set but the clause is still wrong
            #stack.append((clause, i, b))
            true_dic0[abs(b)] = b > 0
            i += 1
            continue
        # Both a, b are set and clause is wrong
        # Then go back
        if len(stack) == 0 or has_backed:
            return 'Unsatisfiable'
        
        last_clause, last_i, last_a = stack.pop()
        (la, lb) = last_clause
        if abs(la) == last_a:
            true_dic0[abs(la)] = not (la > 0)
            true_dic0[abs(lb)] = lb > 0
            #stack.append((clause, i, lb))
        else:
            true_dic0[abs(lb)] = not (lb > 0)
            true_dic0[abs(la)] = la > 0
            #stack.append((clause, i, la))
            
        #print 89, last_i, i
        for cla in data[last_i+1: i]:
            #print 90, cla
            (a, b) = cla
            if abs(a) not in (abs(la), abs(lb)) and true_dic0[abs(a)] != []:
                true_dic0[abs(a)] = []
            if abs(b) not in (abs(la), abs(lb)) and true_dic0[abs(b)] != []:
                true_dic0[abs(b)] = []
        i = last_i
        i += 1
        
    print 81, true_dic0
    unmet_data = verify(true_dic0, data0)
    if len(unmet_data) == 0:
        return 'Found!'
    return 'Not found'
    
        
def papadimitriou():
    n, data0 = load_data()
    print 26, 'data loaded'
    true_dic0 = {}

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
#print papadimitriou()
print backtrack()

print time.time() - start_time
