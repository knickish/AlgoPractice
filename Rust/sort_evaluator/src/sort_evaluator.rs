/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
 
#![allow(unused)]
use rand::{distributions::Uniform, Rng}; // 0.8.0

pub fn evaluate(sorter: fn(i32, &mut Vec<i32>) -> bool) -> bool
{
    for i in 0i32..1000
    {
        println!("Sorting list of length: {}\r", i);
        let range = Uniform::from(-255..256);
        let original: Vec<i32> = rand::thread_rng().sample_iter(&range).take(i as usize).collect();
        let mut sorter_vec = original.to_vec();
        sorter(i, &mut sorter_vec);
        for j in 1usize..(i as usize)
        {
            if sorter_vec[j-1]>sorter_vec[j]
            {
                println!("Out of order element");
                return false;
            }
        }
    }
    println!("Sorter Passed Test");
    return true;
}


