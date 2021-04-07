#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

#testing a parallel sorting algorithm that guarantees factor of 2 balancing across 
#cores with the requirement of good sample distributions.

from sortEvaluator import EvaluateSorter
import multiprocessing
from insertion import insertion
import random
from itertools import repeat

unsorted = [random.randint(0,100) for _ in range(30)]

def swap(list_arg_swap, i_1, i_2):
        tmp = list_arg_swap[i_2]
        list_arg_swap[i_2] = list_arg_swap[i_1]
        list_arg_swap[i_1] = tmp

def psrs_quick(list_arg, l, r):

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
    
    quick_sort(list_arg, l, r)
    return list_arg

def get_pivot_src(list_arg,l_r_tup, p, w):
    l = l_r_tup[0]
    r = l_r_tup[1]
    psrs_quick(list_arg, l, r)
    indices = [1+l+(w*x) for x in range(p)]
    # print("indices:",indices)
    pivot_src = [list_arg[x] for x in indices]
    # print(pivot_src)
    return pivot_src

def multi_partition(list_arg_internal, pivot_vals, l_r_tup):
        l = l_r_tup[0]
        r = l_r_tup[1]
        l_int = l
        r_int = r-1
        l_int_list = []
        for pivot_index, pivot in enumerate(pivot_vals):
            l_int = l
            r_int = r-1
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
            l_int_list.append(l_int)
        
        l_int_list[0] = (l, l_int_list[0])
        for i in range(1,len(l_int_list)):
            l_int_list[i] = (l_int_list[i-1][1], l_int_list[i])
        if l_int_list[-1][1]!=(r-1):
            l_int_list.append((l_int_list[-1][1], (r-1)))
        # print(list_arg_internal[l:r], "partitioned around", pivot_vals)
        return l_int_list



def psrs(list_arg_ext):
# def psrs():
    # cores = multiprocessing.cpu_count()
    # if not cores:
    list_arg = multiprocessing.Manager().list()
    list_arg = list_arg_ext
    cores = 2
    def select_pivots(pivot_list, p, n):
        pi = int(p/(n**2))
        if not pi:
            pi = 1
        pivot_src = insertion(pivot_list)
        pivots = [pivot_src[pi+p*x] for x in range(p)]
        pivots = pivots[1:]
        return pivots
    
    def order_partitions(list_arg, partition_boundaries):
        ordered_parts = [[]*len(partition_boundaries[0])]
        print(list_arg)
        print(partition_boundaries)
        for j in partition_boundaries:
            for i, v in enumerate(j):
                ordered_parts[i] = list_arg[v[0]:v[1]]
        newlist = []
        for i in ordered_parts:
            for j in i:
                newlist.extend(j)
        newBounds = [i[-1] for i in partition_boundaries]
        return newlist, newBounds

    # setup
    if len(list_arg)<2:
        return list_arg
    last_list_index = len(list_arg)-1
    w = int(last_list_index/(cores**2))
    # print(w)
    start_l_r = [(int(i*len(list_arg)/cores), int((1+i)*len(list_arg)/cores)) for i in range(cores)]
    # print(start_l_r)
    with multiprocessing.Pool(processes=cores) as pool:
    #     #get_pivot_src
        nested_list = pool.starmap(get_pivot_src, zip(repeat(list_arg), start_l_r, repeat(cores), repeat(w)))
    pool.join()
    # print(nested_list)
    results = [i for j in nested_list for i in j]
    # print(results)

    #select_pivots
    pivots = select_pivots(results, cores, last_list_index)
    # print(pivots)

    with multiprocessing.Pool(processes=cores) as pool:
    # partition
        partition_boundaries = pool.starmap(multi_partition, zip(repeat(list_arg), repeat(pivots), start_l_r))
    pool.join()
    # print(partition_boundaries)

    

    
    # partition_boundaries = [[]*cores]
    # for i in range(cores):
    #     for j in results[i]:
    #         partition_boundaries[i].append(j)

    new_list, new_boundaries = order_partitions(list_arg, partition_boundaries)


if __name__ == "__main__":
    
    # print(unsorted)
    psrs(unsorted)