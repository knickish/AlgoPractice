#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

a = 1234567

def getNthDigit(num, digit):
    ret = int((num%(10**digit)-num%(10**(digit-1)))/(10**(digit-1)))
    return ret
printVal = getNthDigit(a, 1)
print(printVal)