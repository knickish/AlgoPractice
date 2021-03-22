/*
 *   Copyright (c) 2021 Kirk Nickish
 *   All rights reserved.
 */
use sort_evaluator::sort_evaluator::evaluate;

pub fn counting(_ele_count: i32, elements: &mut Vec<i32>) -> bool {
    if _ele_count < 2 {
        return true;
    }
    let mut _min: i32 = elements[0];
    let mut _max: i32 = elements[0];
    for x in elements.iter() {
        if x < &_min {
            _min = *x;
        }
        if x > &_max {
            _max = *x;
        }
    }
    for x in elements.iter_mut() {
        *x = *x - _min;
    }
    let counting_vec_size:i32 = _max - _min + 1
    let mut counting_vec: Vec<i32> = Vec::with_capacity(counting_vec_size);
    counting_vec.resize(counting_vec_size, 0);
    for x in elements.iter() {
        counting_vec[x]+=1;
    }
    let mut index:usize = 0;
    for (i,v) in counting_vec.iter().enumerate() {
        for _ in 0..(v+1) {
            elements[index] = i;
            index+=1;
        }
    }
    for x in elements.iter_mut() {
        *x = *x + _min;
    }

    return true;
}

fn main() {
    let res: bool = evaluate(counting);
    if res {
        std::process::exit(0x0);
    } else {
        std::process::exit(0x1);
    }
}
