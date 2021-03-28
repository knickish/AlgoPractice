#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def insertion(list_arg):
    def get_min(list_arg_internal, start_index):
        _min = list_arg_internal[0] 
        _min_index = start_index
        for _i, _v in enumerate(list_arg_internal):
            if _v<_min:
                _min = _v
                _min_index = _i+start_index
        return (_min, _min_index)
    for i in range(len(list_arg)):
        v = list_arg[i]
        smallest, index = get_min(list_arg[i:], i)
        if smallest < v:
            list_arg[index] = v
            list_arg[i] = smallest
    return list_arg

model = EvaluateSorter(insertion)
model.evaluate(1000)
    