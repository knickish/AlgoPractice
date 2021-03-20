use sort_evaluator::sort_evaluator::evaluate;

pub fn known_good_sorter(_ele_count: i32, elements: &mut Vec<i32>) -> bool
{
    elements.sort();
    return true;
}

fn main()
{
    let res: bool = evaluate(known_good_sorter);
    if res
    {
        std::process::exit(0x0);
    }
    else
    {
        std::process::exit(0x1);
    }
}