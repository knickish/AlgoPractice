#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def heap(list_arg_ext):
    def lchildindex(index):
        return int((2*index)+1)
    def rchildindex(index):
        return int((2*index)+2)
    def parentindex(index):
        return int((index-1)/2)
    def swap(list_arg_swap, i_1, i_2):
        tmp = list_arg_swap[i_2]
        list_arg_swap[i_2] = list_arg_swap[i_1]
        list_arg_swap[i_1] = tmp
    def heapify(list_arg, start_index, last_list_index):
        index = start_index
            
        rcindex = rchildindex(index)
        lcindex = lchildindex(index)
        lval = list_arg[index]
        rval = lval
        lcheck = False
        rcheck = False
        if rcindex<=last_list_index:
            rval = list_arg[rcindex]
        else:
            rcheck = True
        if lcindex<=last_list_index:
            lval = list_arg[lcindex]
        else:
            lcheck = True
        if lval>rval:
            if lval>list_arg[index]:
                swap(list_arg, lcindex, index)
                heapify(list_arg, lcindex, last_list_index)
            elif rval>list_arg[index]:
                swap(list_arg, rcindex, index)
                heapify(list_arg, rcindex, last_list_index)
        else:
            if rval>list_arg[index]:
                swap(list_arg, rcindex, index)
                heapify(list_arg, rcindex, last_list_index)
            elif lval>list_arg[index]:
                swap(list_arg, lcindex, index)
                heapify(list_arg, lcindex, last_list_index)
        if rcheck and lcheck:
            return
            
    #setup
    if len(list_arg_ext)<2:
        return list_arg_ext
    last_list_index = len(list_arg_ext)-1
    list_arg = list_arg_ext.copy()

    #build max heap
    for i in range(0,len(list_arg_ext)):
        j = last_list_index-i
        heapify(list_arg, j, last_list_index)

    #sort in place using heap
    for i in range(0,len(list_arg_ext)):
        j = last_list_index-i
        swap(list_arg, 0, j)
        heapify(list_arg, 0, last_list_index-(i+1))

    return list_arg
    

if __name__ == "__main__":
    model = EvaluateSorter(heap)
    model.evaluate(1000)