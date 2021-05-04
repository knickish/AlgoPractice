/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
#ifndef sort_evaluator_cpp
#define sort_evaluator_cpp

#include "sort_evaluator.hpp"

void swap(vector<int> &vect, int i_1, int i_2)
{
    int tmp = vect[i_2];
    vect[i_2] = vect[i_1];
    vect[i_1] = tmp;
}

void SortEvaluator::error_out(vector<int> res, vector<int> orig, const char* str)
{
    printf("Sorter Error: %s", str);
    printf("\n");
    printf("Elements Returned: %ld", res.size());
    printf("\n");
    printf("Elements: \n[");
    int linebreak = 0;
    for (int i = 0; i<res.size() ; i++)
    {
        linebreak++;
        if (linebreak%20==0)
            printf("\n");
        printf("%d, ",res[i]);
        
    }
    printf("]\n\n");
    printf("Orig elements Returned: %ld", orig.size());
    printf("\n");
    printf("Orig Elements: \n[");
    linebreak = 0;
    for (int i = 0; i<orig.size() ; i++)
    {
        linebreak++;
        if (linebreak%20==0)
            printf("\n");
        printf("%d, ", orig[i]);
        
    }
    printf("]\n\n");
}

bool SortEvaluator::evaluate(vector<int>  sorter(int ele_count, vector<int> &int_array))
{
    srand (time(NULL));

    for (int i = 0; i<10000 ; i++)
    {
        const int ele_count = i;
        vector<int> arr;
        for (int j = 0; j<=i;j++)
        {
            arr.push_back(rand());
        }
        vector<int> orig = arr;
        vector<int> res = sorter(i, arr);
        if(i+1!=res.size())
        {
            error_out(res, orig, "Element count wrong");
            return false;
        }
        for (int j = 1; j<i;j++)
        {
            if (res[j-1]>res[j])
            {
                printf("\n%d %d\n", res[j-1] ,res[j]);
                error_out(res, orig, "Out of order element");
                return false;
            }
        }
    }
    printf("Sorter passed test\n");
    return true;
}

#endif
