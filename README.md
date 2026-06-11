# Taylor Series Visualizer

A Python project that visualizes how the Taylor series approximates the sine function.

## What This Project Does

The sine function sin(x) is a smooth wave, but computers can only do basic arithmetic.
The Taylor series solves this by adding together simple polynomial terms (x, x³, x⁵ ...)
to approximate sin(x). The more terms you add, the closer the approximation gets.

This project visualizes that process in three steps.

## Files

| File | Description |
|------|-------------|
| `part1_sin_curve.py` | Plots the true sin(x) function |
| `part2_approximation.py` | Overlays Taylor approximations with 1–5 terms |
| `part3_interactive.py` | Interactive slider to control the number of terms in real time |
| `main.py` | Runs all three parts in sequence |

## How to Run

Run all parts in sequence:
python part1_sin_curve.py
python part2_approximation.py
python part3_interactive.py

## Requirements

- Python 3.x
- numpy
- matplotlib
- PyQt5 (required for the interactive slider in Part 3)

Install dependencies:pip install numpy matplotlib PyQt5

## The Math

The Taylor series for sin(x) centered at 0:

sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...

Each term follows the pattern: (-1)^n * x^(2n+1) / (2n+1)!

The series converges for all values of x, but requires more terms
to stay accurate further from the origin.