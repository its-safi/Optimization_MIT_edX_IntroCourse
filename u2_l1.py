# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:54:20 2020

@author: safiu
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        print('value of i',i)
        for j in range(N):
            print('value of j',j,(i >> j),((i >> j)%2))
            # test bit jth of integer i            
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
def bagCeat(items):
    N = len(items)
# enumerate the 2**N possible combinations for bag1
    for i in range(2**N):
        bag1 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
        # enumerate the 2**N possible combinations for bag2
        for k in range(2**N):
            bag2 = []
            for l in range(N):
                # test bit lth of integer k
                if (k >> l) % 2 == 1:
                    bag2.append(items[l])                 
            check = any(item in bag1 for item in bag2)
            if check is False:
                yield (bag1, bag2)

def bagSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        bag1 = []
        bag2 = []
        #print('value of i',i)
        for j in range(N):
            #print('value of j',j,(i >> j),((i >> j)%2))
            # test bit jth of integer i            
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
                bag2.append(items[j])
        
        combo=(bag1,bag2)
        yield combo
        print(len(bag1))
        print(len(bag2))
        
items=['i1','i2','i3']
for n in bagCeat(items):
    print('end' , n); 