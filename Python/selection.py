#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def selection(list_arg_ext):
    def swap(list_arg_swap, i_1, i_2):
        tmp = list_arg_swap[i_2]
        list_arg_swap[i_2] = list_arg_swap[i_1]
        list_arg_swap[i_1] = tmp
   
    #setup
    if len(list_arg_ext)<2:
        return list_arg_ext
    last_list_index = len(list_arg_ext)-1
    list_arg = list_arg_ext.copy()
    list_arg_len = len(list_arg)

    #sort
    for i in range(list_arg_len):
        largest = list_arg[0]
        largest_index = 0
        for ii in range(1,list_arg_len-i):
            if largest<list_arg[ii]:
                largest = list_arg[ii]
                largest_index = ii
        swap(list_arg, list_arg_len-(i+1), largest_index)

    return list_arg
    

if __name__ == "__main__":
    model = EvaluateSorter(selection)
    model.evaluate(1000)