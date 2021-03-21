/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

struct sorter_result_s
{
    int     ele_count;
    int*    first_ele;
};

typedef struct sorter_result_s sorter_result;

bool evaluateSorter(sorter_result sorter(int ele_count, int* int_array));

void error_out(sorter_result res, sorter_result orig, const char* str);