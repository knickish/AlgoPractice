#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def merge(list_arg):
    def zip_lists(first_list, second_list):
        zipped = []
        zip_index = 0
        first_index = 0
        second_index = 0
        first_size = len(first_list)
        second_size = len(second_list)
        while True:
            if first_index<first_size:
                if second_index<second_size:
                    if first_list[first_index]<second_list[second_index]:
                        zipped.append(first_list[first_index])
                        first_index+=1
                    else:
                        zipped.append(second_list[second_index])
                        second_index+=1
                else:
                    zipped.append(first_list[first_index])
                    first_index+=1
            else:
                if second_index<second_size:
                    zipped.append(second_list[second_index])
                    second_index+=1
                else:
                    return zipped

    def merge_sort(list_arg):
        split = int(len(list_arg)/2)
        while split:
            first = merge_sort(list_arg[:split]) 
            second = merge_sort(list_arg[split:])
            return zip_lists(first, second)
        return list_arg
    
    return merge_sort(list_arg)
            
if __name__ == "__main__":
    model = EvaluateSorter(merge)
    model.evaluate(1000)