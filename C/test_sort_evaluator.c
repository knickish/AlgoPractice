/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
#include "sort_evaluator.h"

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

sorter_result known_good_sorter(int ele_count, int* int_array)
{
    sorter_result ret = {0};
    qsort(int_array, ele_count, sizeof(int), cmpfunc);
    ret.ele_count = ele_count;
    ret.first_ele = int_array;
    return ret;
}

int main(void)
{
    if(evaluateSorter(known_good_sorter))
        return 0;
    else;
        return 1;
}