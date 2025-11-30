//! Advent of Code 2025 - CLI Entry Point
//!
//! Usage:
//!   cargo run -- solve <day> [--part <1|2>]
//!   cargo run -- download <day>
//!   cargo run -- new <day>

use clap::{Parser, Subcommand};
use std::time::Instant;

use aoc2025_rust::{days, input, scaffold};

#[derive(Parser)]
#[command(name = "aoc2025")]
#[command(about = "Advent of Code 2025 Solutions in Rust")]
#[command(version)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Run a specific day's solution
    Solve {
        /// Day number (1-25)
        #[arg(value_parser = clap::value_parser!(u8).range(1..=25))]
        day: u8,

        /// Run only part 1 or 2 (runs both if not specified)
        #[arg(short, long, value_parser = clap::value_parser!(u8).range(1..=2))]
        part: Option<u8>,
    },

    /// Download input for a day
    Download {
        /// Day number (1-25)
        #[arg(value_parser = clap::value_parser!(u8).range(1..=25))]
        day: u8,
    },

    /// Scaffold a new day's solution files
    New {
        /// Day number (1-25)
        #[arg(value_parser = clap::value_parser!(u8).range(1..=25))]
        day: u8,
    },
}

fn main() {
    // Load .env file from project root if it exists
    let _ = dotenvy::from_path("../.env");

    let cli = Cli::parse();

    match cli.command {
        Commands::Solve { day, part } => run_solve(day, part),
        Commands::Download { day } => run_download(day),
        Commands::New { day } => run_new(day),
    }
}

fn run_solve(day: u8, part: Option<u8>) {
    println!("🎄 Advent of Code 2025 - Day {:02}", day);
    println!("{}", "=".repeat(40));

    // Get input (auto-download if missing)
    let input = match input::get_input(day) {
        Ok(content) => content,
        Err(e) => {
            eprintln!("❌ Failed to get input: {}", e);
            std::process::exit(1);
        }
    };

    // Run the solution(s)
    match part {
        Some(1) => run_part(day, 1, &input),
        Some(2) => run_part(day, 2, &input),
        None => {
            run_part(day, 1, &input);
            println!();
            run_part(day, 2, &input);
        }
        _ => unreachable!(),
    }
}

fn run_part(day: u8, part: u8, input: &str) {
    let start = Instant::now();
    let result = days::run_day(day, part, input);
    let elapsed = start.elapsed();

    match result {
        Some(answer) => {
            println!("Part {}: {}", part, answer);
            println!("  ⏱️  {:.3}ms", elapsed.as_secs_f64() * 1000.0);
        }
        None => {
            println!("Part {}: Not implemented yet", part);
        }
    }
}

fn run_download(day: u8) {
    println!("📥 Downloading input for Day {:02}...", day);

    match input::download_input(day) {
        Ok(path) => println!("✅ Input saved to: {}", path),
        Err(e) => {
            eprintln!("❌ Failed to download: {}", e);
            std::process::exit(1);
        }
    }
}

fn run_new(day: u8) {
    println!("🆕 Scaffolding Day {:02}...", day);

    match scaffold::scaffold_day(day) {
        Ok(()) => println!("✅ Day {:02} scaffolded successfully!", day),
        Err(e) => {
            eprintln!("❌ Failed to scaffold: {}", e);
            std::process::exit(1);
        }
    }
}
