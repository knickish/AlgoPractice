/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */

#include "sort_evaluator.hpp"

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

vector<int>  known_good_sorter(int ele_count, vector<int> &int_array_arg)
{
    vector<int> int_array = int_array_arg;
    std::sort(int_array.begin(), int_array.end());
    return int_array;
}

int main(void)
{
    SortEvaluator ev;
    if(ev.evaluate(known_good_sorter))
        return 0;
    else;
        return 1;
}