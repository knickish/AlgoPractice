/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */

#include "sort_evaluator.hpp"
#include "insertion.hpp"

vector<int> insertion(int ele_count, vector<int> &int_array)
{
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
    return int_array;
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