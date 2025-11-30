//! Day modules for Advent of Code 2025
//!
//! Each day is implemented as a separate module.

pub mod day01;

/// Run a specific day and part, returning the result
///
/// # Arguments
/// * `day` - Day number (1-25)
/// * `part` - Part number (1 or 2)
/// * `input` - The puzzle input as a string
///
/// # Returns
/// * `Some(answer)` if the solution is implemented
/// * `None` if the solution is not yet implemented
pub fn run_day(day: u8, part: u8, input: &str) -> Option<i64> {
    match day {
        1 => match part {
            1 => day01::part_one(input).map(|v| v as i64),
            2 => day01::part_two(input).map(|v| v as i64),
            _ => None,
        },
        // Add new days here as they are implemented:
        // 2 => match part {
        //     1 => day02::part_one(input).map(|v| v as i64),
        //     2 => day02::part_two(input).map(|v| v as i64),
        //     _ => None,
        // },
        _ => {
            eprintln!("Day {} is not implemented yet", day);
            None
        }
    }
}
