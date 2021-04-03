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
        print(f"swapping {list_arg_swap[i_2]} and {list_arg_swap[i_1]} in {list_arg_swap}")
        tmp = list_arg_swap[i_2]
        list_arg_swap[i_2] = list_arg_swap[i_1]
        list_arg_swap[i_1] = tmp
    def heapify(list_arg, start_index, last_list_index):
        index = start_index
        
        while True:
            rcindex = rchildindex(index)
            lcindex = lchildindex(index)
            print(f"Heapify {list_arg[start_index]} at {start_index} in {list_arg} rcindex = {rcindex} lcindex = {lcindex}")
            if rcindex<=last_list_index:
                if list_arg[rcindex]<list_arg[index]:
                    swap(list_arg, index, rcindex)
                    index = rcindex
                    continue
            elif lcindex<=last_list_index:
                if list_arg[lcindex]>list_arg[index]:
                    swap(list_arg, index, lcindex)
                    index = lcindex
                    continue
            else:
                break
    if len(list_arg_ext)<2:
        return list_arg_ext
    last_list_index = len(list_arg_ext)-1
    list_arg = list_arg_ext.copy()
    for i in range(0,len(list_arg_ext)):
        j = last_list_index-i
        heapify(list_arg, j, last_list_index)

    for i in range(0,len(list_arg_ext)):
        j = last_list_index-i
        swap(list_arg, 0, j)
        heapify(list_arg, j, )
    

    return list_arg
    

if __name__ == "__main__":
    model = EvaluateSorter(heap)
    model.evaluate(1000)