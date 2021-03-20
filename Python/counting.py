def counting(list_arg):
    if len(list_arg)<2:
        return list_arg
    _min = list_arg[0]
    _max = list_arg[0]
    for i, v in enumerate(list_arg):
        if v < _min:
            _min = v
        if v > _max:
            _max = v
    arr = [0 ] * (_max-_min+1)
    for i in list_arg:
        arr[i-_min]+=1
    retList = []
    for i, v in enumerate(arr):
        for _ in range(v):
            retList.append(i)
    return retList
