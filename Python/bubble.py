#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def bubble(list_arg_ext):
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
        for ii in range(1,list_arg_len-i):
            if list_arg[ii]<list_arg[ii-1]:
                swap(list_arg, ii, ii-1)

    return list_arg
    

if __name__ == "__main__":
    model = EvaluateSorter(bubble)
    model.evaluate(1000)