#
#  Copyright (c) 2021 Kirk Nickish
#  All rights reserved.
#

import random
from pprint import pprint
import traceback

class EvaluateSorter:
    def __init__(self, sorter):
        self.testSet = None
        self.sortedSet = None
        self.sort_func = sorter

    def replace_sorter(self, sorter):
        self.sort_func = sorter

    def generate_element_dict(self, list_arg):
        ret = {}
        for i, v in enumerate(list_arg):
            if v in ret:
                ret[v]+=1
            else:
                ret[v]=1
        return ret

    def error_out(self, str_arg):
        pprint(self.testSet)
        pprint(self.sortedSet)
        raise Exception(str_arg)

    
    def evaluate(self, iterations):
        try:
            for i in range(iterations):
                print(f"Running test on list of length {i}", end="\r")
                self.testSet = [random.randint(-255,255) for _ in range(i)]
                self.sortedSet = self.sort_func(self.testSet)
                if (len(self.sortedSet)!=len(self.testSet)):
                    self.error_out("\nlists are of different length")
                prevVal = -256
                if self.generate_element_dict(self.testSet)!=self.generate_element_dict(self.sortedSet):
                    print(self.generate_element_dict(self.testSet),self.generate_element_dict(self.sortedSet))
                    self.error_out("\nList contains different numbers")
                for index, value in enumerate(self.sortedSet):
                    if value<prevVal:
                        self.error_out(f"\nOut of order element {value} at index {index}")
                    prevVal = value
            print("\nsorter was successful\n")
            return True
        except:
            traceback.print_exc(file=sys.stdout)
            self.error_out("\nError in sorter logic\n")
        


        