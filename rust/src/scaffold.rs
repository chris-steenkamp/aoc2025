//! Scaffolding for new day solutions
//!
//! Creates the necessary files for a new day's solution.

use std::fs;
use std::path::PathBuf;

/// Scaffold a new day's solution files
pub fn scaffold_day(day: u8) -> Result<(), Box<dyn std::error::Error>> {
    let day_str = format!("{:02}", day);

    // Create the day module file
    let day_path = PathBuf::from(format!("src/days/day{}.rs", day_str));
    if day_path.exists() {
        return Err(format!("Day {} module already exists at {:?}", day, day_path).into());
    }

    let day_template = generate_day_template(day);
    fs::write(&day_path, day_template)?;
    println!("  📄 Created: {:?}", day_path);

    // Create the example input file
    let example_path = PathBuf::from(format!("../data/examples/{}.txt", day_str));
    if !example_path.exists() {
        if let Some(parent) = example_path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(&example_path, "# Paste example input here\n")?;
        println!("  📄 Created: {:?}", example_path);
    }

    // Print instructions for manual step
    println!();
    println!("📝 Manual step required:");
    println!("   Add the following line to src/days/mod.rs:");
    println!();
    println!("   pub mod day{};", day_str);
    println!();
    println!("   And add a match arm in the run_day function:");
    println!();
    println!("   {} => match part {{", day);
    println!("       1 => day{}::part_one(input).map(|v| v as i64),", day_str);
    println!("       2 => day{}::part_two(input).map(|v| v as i64),", day_str);
    println!("       _ => None,");
    println!("   }},");

    Ok(())
}

fn generate_day_template(day: u8) -> String {
    let day_str = format!("{:02}", day);
    format!(
        r#"//! Day {day}: [Title]
//!
//! https://adventofcode.com/2025/day/{day}

/// Solve part one
pub fn part_one(input: &str) -> Option<u64> {{
    let _lines: Vec<&str> = input.lines().collect();
    
    // TODO: Implement solution
    None
}}

/// Solve part two
pub fn part_two(input: &str) -> Option<u64> {{
    let _lines: Vec<&str> = input.lines().collect();
    
    // TODO: Implement solution
    None
}}

#[cfg(test)]
mod tests {{
    use super::*;

    fn example_input() -> String {{
        std::fs::read_to_string("../data/examples/{day_str}.txt")
            .expect("Failed to read example input")
    }}

    #[test]
    fn test_part_one() {{
        let input = example_input();
        // TODO: Update expected value from puzzle description
        assert_eq!(part_one(&input), None);
    }}

    #[test]
    fn test_part_two() {{
        let input = example_input();
        // TODO: Update expected value from puzzle description
        assert_eq!(part_two(&input), None);
    }}
}}
"#,
        day = day,
        day_str = day_str,
    )
}
