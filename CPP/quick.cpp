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



vector<int> gen_rand_pivots(int l, int r, std::mt19937 randomizer)
{
    std::uniform_int_distribution<int> dist {l, r};
    auto generator_func = [&dist, &randomizer]()
        {
            return dist(randomizer);
        };

    vector<int> vec(3);
    std::generate(begin(vec), end(vec), generator_func);
    return vec;
}

int pivot3rand(vector<int> &list_arg_internal, int l, int r, std::mt19937 randomizer)
{
    vector<int> pivotindexes = gen_rand_pivots(l,r, randomizer);
    
    vector<int> pivots(3);
    for (int i = 0 ; i < pivotindexes.size(); i++)
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

int partition(vector<int> &list_arg_internal, int l, int r, std::mt19937 randomizer)     
{
    int l_int = l;
    int r_int = r-1;
    int pivotIndex = pivot3rand(list_arg_internal, l, r_int, randomizer);
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

void quick_sort(vector<int> &list_arg_internal, int _l, int _r, std::mt19937 randomizer)
{
    
    if ((_r-_l)>1)
    {
        int partition_index = partition(list_arg_internal, _l, _r, randomizer);
        quick_sort(list_arg_internal, _l, partition_index, randomizer);
        quick_sort(list_arg_internal, partition_index+1, _r, randomizer);
    }
}
            

vector<int> quick(int ele_count, vector<int> &int_array_arg)
{
    std::random_device rnd_device;
    std::mt19937 mersenne_twister {rnd_device()};
    quick_sort(int_array_arg, 0, int_array_arg.size()-1, mersenne_twister);
    return int_array_arg;
}

int main(void)
{
    SortEvaluator ev;
    if(ev.evaluate(quick))
        return 0;
    else;
        return 1;
}