use std::io;

fn main() {
    let mut a = String::new();
    let mut b = String::new();

    io::stdin().read_line(&mut a)
        .expect("Failed to read line a");
    io::stdin().read_line(&mut b)
        .expect("Failed to read line b");

    let a: i32 = a.trim().parse()
        .expect("Please type a number a!");
    let b: i32 = b.trim().parse()
        .expect("Please type a number b!");

    println!("{}", a * b);   
}