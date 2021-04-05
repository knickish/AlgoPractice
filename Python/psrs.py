#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

#testing a parallel sorting algorithm that guarantees factor of 2 balancing across 
#cores with the requirement of good sample distributions.

from sortEvaluator import EvaluateSorter
import multiprocessing
from insertion import insertion

def psrs_quick(list_arg):
    def swap(list_arg_swap, i_1, i_2):
        tmp = list_arg_swap[i_2]
        list_arg_swap[i_2] = list_arg_swap[i_1]
        list_arg_swap[i_1] = tmp
        # return

    def partition(list_arg_internal, l, r):
        def pivot3rand(l, r):
            pivotindexes = [random.randint(l,r) for _ in range(3)]
            pivots = [list_arg_internal[x] for x in pivotindexes]
            piv_dict = dict(zip(pivots, pivotindexes)).copy()
            pivots = insertion(pivots)
            return piv_dict[pivots[1]]
        l_int = l
        r_int = r-1
        pivotIndex = pivot3rand(l, r_int)
        pivot = list_arg_internal[pivotIndex]
        swap(list_arg_internal, pivotIndex, r_int)
        r_int= r_int-1
        while l_int<=r_int:
            while l_int<=r_int:
                if list_arg_internal[l_int]>=pivot:
                    break
                else:
                    l_int+=1
            while l_int<=r_int:
                if list_arg_internal[r_int]<pivot:
                    break
                else:
                    r_int-=1
            if l_int<r_int:                    
                swap(list_arg_internal, l_int, r_int)
            else:
                break
        swap(list_arg_internal, l_int, r-1)
        return l_int
    
    def quick_sort(list_arg_internal, _l, _r):
        if (_r-_l)>1:
            partition_index = partition(list_arg_internal, _l, _r)
            quick_sort(list_arg_internal, _l, partition_index) 
            quick_sort(list_arg_internal, partition_index+1, _r)
        #return
    
    quick_sort(list_arg, 0, len(list_arg))
    return list_arg

def psrs(list_arg):
    cores = multiprocessing.cpu_count()
    if not cores:
        cores = 2
    def get_pivots(list_arg, p, w):
        psrs_quick(list_arg)
        


    def split_list(listLen, p):
        
    
    #setup
    if len(list_arg)<2:
        return list_arg
    last_list_index = len(list_arg)-1
    w = n/(p**2)

