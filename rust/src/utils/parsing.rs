//! Parsing utilities for Advent of Code
//!
//! Common functions for parsing puzzle inputs.

use regex::Regex;

/// Parse all integers (positive and negative) from a string
pub fn parse_numbers(input: &str) -> Vec<i64> {
    let re = Regex::new(r"-?\d+").unwrap();
    re.find_iter(input)
        .filter_map(|m| m.as_str().parse().ok())
        .collect()
}

/// Parse all unsigned integers from a string
pub fn parse_unsigned(input: &str) -> Vec<u64> {
    let re = Regex::new(r"\d+").unwrap();
    re.find_iter(input)
        .filter_map(|m| m.as_str().parse().ok())
        .collect()
}

/// Parse input into a 2D grid of characters
pub fn parse_grid(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| line.chars().collect())
        .collect()
}

/// Parse input into lines, filtering empty lines
pub fn parse_lines(input: &str) -> Vec<&str> {
    input.lines().filter(|line| !line.is_empty()).collect()
}

/// Parse input into groups separated by blank lines
pub fn parse_groups(input: &str) -> Vec<&str> {
    input.split("\n\n").filter(|s| !s.is_empty()).collect()
}

/// Parse a line of space-separated numbers
pub fn parse_line_numbers(line: &str) -> Vec<i64> {
    line.split_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect()
}

/// Parse a line of comma-separated numbers
pub fn parse_csv_numbers(line: &str) -> Vec<i64> {
    line.split(',')
        .filter_map(|s| s.trim().parse().ok())
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_numbers() {
        assert_eq!(parse_numbers("abc 123 def -45 ghi"), vec![123, -45]);
        assert_eq!(parse_numbers("no numbers here"), Vec::<i64>::new());
    }

    #[test]
    fn test_parse_grid() {
        let input = "abc\ndef\nghi";
        let grid = parse_grid(input);
        assert_eq!(grid.len(), 3);
        assert_eq!(grid[0], vec!['a', 'b', 'c']);
    }

    #[test]
    fn test_parse_groups() {
        let input = "group1\n\ngroup2\n\ngroup3";
        let groups = parse_groups(input);
        assert_eq!(groups.len(), 3);
    }
}
