#ifndef sort_evaluator_hpp
#define sort_evaluator_hpp


#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include<algorithm>

struct sorter_result_s
{
    int     ele_count;
    int*    first_ele;
};

typedef struct sorter_result_s sorter_result;

class SortEvaluator
{
    public:

    void error_out(sorter_result res, sorter_result orig, const char* str);

    bool evaluate(sorter_result sorter(int ele_count, int* int_array));

};

#endif