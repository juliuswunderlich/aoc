use std::fs;

/* 
fn part_one() {
    let input = fs::read_to_string("input.txt").expect("File read error");
    let lines: Vec<&str> = input.lines().collect();
    let mut pairs_left: Vec<i32> = vec![];
    let mut pairs_right: Vec<i32> = vec![];
    for line in &lines {
        let numbers: Vec<i32> = line.split_whitespace()
                                .map(|l| l.parse::<i32>().unwrap())
                                .collect();
        assert!(numbers.len() == 2);
        pairs_left.push(numbers[0]);
        pairs_right.push(numbers[1]);
    }
    pairs_left.sort();
    pairs_right.sort();
    let pairs : Vec<(&i32,&i32)> = pairs_left.iter().zip(pairs_right.iter()).collect();
    let result: Vec<i32> = pairs.iter().map(|(&l,&r)| i32::abs(l-r)).collect();
    println!("{:?}", result.iter().sum::<i32>());
}
*/
use std::collections::HashMap;

fn main() {
    let input = fs::read_to_string("input.txt").expect("File read error");
    let lines: Vec<&str> = input.lines().collect();
    let mut pairs_left: Vec<i32> = vec![];
    let mut pairs_right: Vec<i32> = vec![];
    for line in &lines {
        let numbers: Vec<i32> = line.split_whitespace()
                                .map(|l| l.parse::<i32>().unwrap())
                                .collect();
        assert!(numbers.len() == 2);
        pairs_left.push(numbers[0]);
        pairs_right.push(numbers[1]);
    }
    pairs_left.sort();
    pairs_right.sort();
    let pairs : Vec<(&i32,&i32)> = pairs_left.iter().zip(pairs_right.iter()).collect();

    let mut counter_right = HashMap::new();
    for num in pairs_right {
        println!("{:?}", num);
        let counter = counter_right.entry(num).or_insert(0);
        *counter += 1;
    }
    let mut final_sum = 0;
    for num in pairs_left {
        let count = counter_right.get(&num).unwrap_or(&0);
        final_sum += num * count;
    }

    println!("{:?}", final_sum);
}