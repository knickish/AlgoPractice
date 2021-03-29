#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

import random
from insertion import insertion
from sortEvaluator import EvaluateSorter

def quick(list_arg):
    list_arg_copy = list_arg.copy()
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
    
    quick_sort(list_arg_copy, 0, len(list_arg_copy))
    return list_arg_copy


if __name__ == "__main__":
    model = EvaluateSorter(quick)
    model.evaluate(1000)  

