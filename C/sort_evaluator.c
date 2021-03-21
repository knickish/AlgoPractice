/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
#include "sort_evaluator.h"

bool evaluateSorter(sorter_result sorter(int ele_count, int* int_array))
{
    time_t t;
    srand((unsigned) time(&t));

    for (int i = 0; i<1000 ; i++)
    {
        const int ele_count = i;
        int* arr = malloc(sizeof(int)*i);
        int* arr_orig = malloc(sizeof(int)*i);
        for (int j = 0; j<=i;j++)
        {
            *(arr+j) = (rand()%512)-256;
        }
        memcpy(arr_orig, arr, sizeof(int)*i);
        sorter_result orig = {i, arr_orig};
        sorter_result res = sorter(i, arr);
        if(i!=res.ele_count)
        {
            error_out(res, orig, "Element count wrong");
            return false;
        }
        for (int j = 1; j<i;j++)
        {
            if (*(arr+(j-1))>*(arr+j))
            {
                printf("\n%d %d\n" ,*(arr+j), *(arr+j-1));
                error_out(res, orig, "Out of order element");
                return false;
            }
        }
        free(arr);
        free(arr_orig);
    }
    printf("Sorter passed test\n");
    return true;
}

void error_out(sorter_result res, sorter_result orig, const char* str)
{
    printf("Sorter Error: %s", str);
    printf("\n");
    printf("Elements Returned: %d", res.ele_count);
    printf("\n");
    printf("Elements: \n[");
    int linebreak = 0;
    for (int i = 0; i<res.ele_count ; i++)
    {
        linebreak++;
        if (linebreak%20==0)
            printf("\n");
        printf("%d, ",*(res.first_ele+i));
        
    }
    printf("]\n\n");
    printf("Orig elements Returned: %d", orig.ele_count);
    printf("\n");
    printf("Orig Elements: \n[");
    linebreak = 0;
    for (int i = 0; i<orig.ele_count ; i++)
    {
        linebreak++;
        if (linebreak%20==0)
            printf("\n");
        printf("%d, ",*(orig.first_ele+i));
        
    }
    printf("]\n\n");
}