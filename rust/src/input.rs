//! Input downloading and management for Advent of Code 2025
//!
//! Downloads puzzle inputs from adventofcode.com using the AOC_SESSION environment variable.

use std::env;
use std::fs;
use std::path::PathBuf;

const AOC_YEAR: u16 = 2025;

/// Get the path to the input file for a given day
pub fn input_path(day: u8) -> PathBuf {
    PathBuf::from(format!("../data/inputs/{:02}.txt", day))
}

/// Get the input for a given day, downloading if necessary
pub fn get_input(day: u8) -> Result<String, Box<dyn std::error::Error>> {
    let path = input_path(day);

    if path.exists() {
        Ok(fs::read_to_string(&path)?)
    } else {
        println!("📥 Input not found, downloading...");
        download_input(day)?;
        Ok(fs::read_to_string(&path)?)
    }
}

/// Download the input for a given day from adventofcode.com
pub fn download_input(day: u8) -> Result<String, Box<dyn std::error::Error>> {
    let session = env::var("AOC_SESSION").map_err(|_| {
        "AOC_SESSION environment variable not set.\n\
         Set it with: $env:AOC_SESSION=\"your_session_cookie_value\"\n\
         Get the value from your browser's cookies at adventofcode.com"
    })?;

    let url = format!(
        "https://adventofcode.com/{}/day/{}/input",
        AOC_YEAR, day
    );

    let client = reqwest::blocking::Client::new();
    let response = client
        .get(&url)
        .header("Cookie", format!("session={}", session))
        .header(
            "User-Agent",
            "github.com/yourusername/aoc2025 by your@email.com",
        )
        .send()?;

    if !response.status().is_success() {
        return Err(format!(
            "Failed to download input: HTTP {} - {}",
            response.status(),
            response.text().unwrap_or_default()
        )
        .into());
    }

    let content = response.text()?;
    let path = input_path(day);

    // Ensure the directory exists
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent)?;
    }

    fs::write(&path, &content)?;

    Ok(path.to_string_lossy().to_string())
}
