/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
#ifndef sort_evaluator_hpp
#define sort_evaluator_hpp


#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>    // std::sort
#include <vector>       // std::vector

using std::vector;

class SortEvaluator
{
    public:

    void error_out(vector<int> res, vector<int>  orig, const char* str);

    bool evaluate(vector<int>  sorter(int ele_count, vector<int> &int_array));

};

void swap(vector<int> &vect, int i_1, int i_2);

#endif