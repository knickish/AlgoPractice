/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */

#include "sort_evaluator.hpp"
#include "insertion.hpp"

void swap(int* int_array, int i_1, int i_2)
{
    int tmp = int_array[i_2];
    int_array[i_2] = int_array[i_1];
    int_array[i_1] = tmp;
}

sorter_result insertion(int ele_count, int* int_array)
{
    sorter_result ret = {0};
    for (int i = 0 ; i < ele_count-1 ; i++)
    {
        int l = int_array[i];
        int lowest = l;
        int lowest_index = i;
        for ( int j = i+1 ; j<ele_count ; j++)
        {
            int r = int_array[j];
            if (r<lowest)
            {
                lowest = r;
                lowest_index = j;
            }
            
        }
        swap(int_array, i, lowest_index);
    }
    ret.ele_count = ele_count;
    ret.first_ele = int_array;
    return ret;
}

#ifdef __main__
int main(void)
{
    SortEvaluator ev;
    if(ev.evaluate(insertion))
        return 0;
    else;
        return 1;
}
#endif