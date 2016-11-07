import time
import math
import random
import copy

start_time = time.time()

def load_data():
    file_name = '2SAT2.txt'
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
    while i < len(data0):
        clause = data0[i]
        (a, b) = clause
        bool_a = False
        bool_b = False
        if (a > 0 and true_dic0[a] == True) or (a < 0 and true_dic0[-a] == False):
            bool_a = True
        if (b > 0 and true_dic0[b] == True) or (b < 0 and true_dic0[-b] == False):
            bool_b = False
        if bool_a or bool_b:
            i += 1
            continue
        # Then the clause is false. 
        if true_dic0[abs(a)] == []:
            # Default to 1st
            stack.append((clause, i, a))
            true_dic0[abs(a)] = a > 0
            i += 1
            continue
        if true_dic0[abs(b)] == []:
            # a is set but the clause is still wrong
            #stack.append((clause, i, b))
            true_dic0[abs(b)] = b > 0
            i += 1
            continue
        # Both a, b are set and clause is wrong
        # Then go back
        if len(stack) == 0:
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
        
    #print 81, stack
    unmet_data = verify(true_dic0, data0)
    if len(unmet_data) == 0:
        return 'Found!'
    return 'Not found'
    
n, data = load_data()
#print papadimitriou()
print backtrack()

print time.time() - start_time
