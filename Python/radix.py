#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter

def radix10(_list_arg):

    def getNthDigit(num, digit):
        if (10**(digit-1))>num:
            return 0
        ret = int((num%(10**digit)-num%(10**(digit-1)))/(10**(digit-1)))
        return ret

    list_arg = _list_arg.copy()
    if len(list_arg)<2:
        return list_arg
    base = 10
    power = 0
    _min = list_arg[0]
    _max = list_arg[0]
    for i, v in enumerate(list_arg):
        if v < _min:
            _min = v
        if v > _max:
            _max = v
    for i,v in enumerate(list_arg):
        list_arg[i] = v- _min
    while base**power<(_max-_min):
        power+=1

    for digit_index in range(1, power+1):
        prepass = [ 0 for _ in range(base+1)]
        new_list_arg = [None for _ in range(len(list_arg))]
        for j in list_arg:
            prepass[getNthDigit(j, digit_index)]+=1
        prepass[0]-=1
        for j in range(1,len(prepass)):
            prepass[j] = prepass[j]+prepass[j-1]
        for j in range(len(list_arg)-1,-1,-1):
            j_val = list_arg[j]
            j_digit = getNthDigit(j_val, digit_index)
            j_newloc = prepass[j_digit]
            new_list_arg[j_newloc] = j_val
            prepass[j_digit]-=1
        list_arg = new_list_arg
       
    for i,v in enumerate(list_arg):
        list_arg[i] = v + _min
        
    return list_arg

model = EvaluateSorter(radix10)
model.evaluate(1000)