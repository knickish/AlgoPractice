#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

from sortEvaluator import EvaluateSorter
import copy
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def testSorter(list_arg):
    internal = list_arg.copy()
    internal.sort()
    return internal

def testFailSort(list_arg):
    return list_arg

blockPrint()
model = EvaluateSorter(testSorter)
model.evaluate(1000)


try:
    model.replace_sorter(testFailSort)
    model.evaluate(1000)
    raise Exception("Fail model passed evaluation?????")
except:
    enablePrint()

