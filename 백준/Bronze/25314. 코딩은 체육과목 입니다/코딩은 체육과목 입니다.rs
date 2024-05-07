use std::io;

fn main() {
    let char_long: String = String::from("long ");
    let mut n = String::new();

    io::stdin().read_line(&mut n)
        .expect("Failed to read line a");
    let n: i32 = n.trim().parse()
        .expect("Please type a number a!");

    let repeat = char_long.repeat((n / 4) as usize);

    println!("{}int", repeat);
}