/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */

#include <thread>
#include <iostream>
#include <vector>
#include <random>
#include <functional>
#include <unordered_map>
#include "sort_evaluator.hpp"
#include "insertion.hpp"

typedef std::unordered_map<int, int> intmap;

void swap(vector<int> &vect, int i_1, int i_2)
{
    int tmp = vect[i_2];
    vect[i_2] = vect[i_1];
    vect[i_1] = tmp;
}

vector<int> gen_rand_pivots(int l, int r)
{
    std::random_device rnd_device;
    std::mt19937 mersenne_twister {rnd_device()};
    std::uniform_int_distribution<int> dist {l, r};

    auto generator_func = [&dist, &mersenne_twister]()
        {
            return dist(mersenne_twister);
        };

    vector<int> vec(3);
    std::generate(begin(vec), end(vec), generator_func);
    return vec;
}

int pivot3rand(vector<int> &list_arg_internal, int l, int r)
{
    vector<int> pivotindexes = gen_rand_pivots(l,r);
    vector<int> pivots(3);
    for (int i = 0 ; i < pivots.size(); i++)
    {
        pivots.push_back( list_arg_internal[pivotindexes[i]]);
    }
    intmap dict;
    for (int i = 0 ; i<pivots.size();i++)
    {
        dict.emplace(pivots[i], pivotindexes[i]);
    }
    vector<int> sorted = pivots;
    insertion(3, sorted);
    return dict[sorted[1]];
}

int partition(vector<int> &list_arg_internal, int l, int r)     
{
    int l_int = l;
    int r_int = r-1;
    int pivotIndex = pivot3rand(list_arg_internal, l, r_int);
    int pivot = list_arg_internal[pivotIndex];
    swap(list_arg_internal, pivotIndex, r_int);
    r_int= r_int-1;
    while (l_int<=r_int)
    {
        while (l_int<=r_int)
        {
            if( list_arg_internal[l_int]>=pivot)
                break;
            else
                l_int+=1;
        }
        while (l_int<=r_int)
        {
            if (list_arg_internal[r_int]<pivot)
                break;
            else
                r_int-=1;
        }
        if (l_int<r_int)                    
            swap(list_arg_internal, l_int, r_int);
        else
            break;
    }
    swap(list_arg_internal, l_int, r-1);
    return l_int;
}

void quick_sort(vector<int> &list_arg_internal, int _l, int _r)
{
    if ((_r-_l)>1)
    {
        int partition_index = partition(list_arg_internal, _l, _r);
        quick_sort(list_arg_internal, _l, partition_index);
        quick_sort(list_arg_internal, partition_index+1, _r);
    }
}
            

void psrs(vector<int> &list_arg, int l, int r)
{
    quick_sort(list_arg, l, r);
}

int main(void)
{
    SortEvaluator ev;
    if(ev.evaluate(psrs))
        return 0;
    else;
        return 1;
}