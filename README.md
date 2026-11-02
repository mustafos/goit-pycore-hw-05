# Python Core — Homework 05

A collection of Python exercises focused on functional programming, recursion, generators, decorators, and built-in modules.

## Overview

This repository contains solutions to the fifth homework assignment of the GoIT Python Core course.

The main goal is to practice Python fundamentals and explore functional programming concepts through practical tasks.

## Tasks

### Task 1 — Caching Fibonacci

Implemented a recursive Fibonacci function using closures and caching.

**Concepts:**

- Closures
- Recursion
- Dictionaries
- Memoization

**File:** `task1.py`

### Task 2 — Generator Numbers

Implemented a generator that extracts decimal numbers from text and calculates their total sum.

**Concepts:**

- Generators
- `yield`
- Regular expressions
- `Callable`
- Functional programming

**File:** `task2.py`

### Task 3 — Log Analyzer (Optional)

Implemented a command-line tool for parsing and analyzing log files.

The application can:

- Read log files.
- Parse individual log entries.
- Count entries by logging level.
- Filter logs by a specific level.
- Handle file reading errors.

**Concepts:**

- File handling
- Lambda functions
- `filter()`
- Command-line arguments
- Exception handling

**Files:** `task3.py`, `log.txt`

### Task 4 — Console Assistant with Decorators

Extended a console-based contact management assistant with error handling using decorators.

The application supports:

- Adding contacts.
- Updating phone numbers.
- Searching for contacts.
- Displaying all contacts.
- Handling invalid user input.

**Concepts:**

- Decorators
- `*args` and `**kwargs`
- Exception handling
- `KeyError`, `ValueError`, `IndexError`

**File:** `task4.py`

## Project Structure

```text
goit-pycore-hw-05/
│
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── log.txt
└── README.md
```

## Requirements

- Python 3.10+
- No external dependencies required.

## How to Run

Run each task independently:

```bash
python3 task1.py
python3 task2.py
python3 task3.py log.txt
python3 task3.py log.txt error
python3 task4.py
```

## Technologies

- Python
- Regular Expressions (`re`)
- Functional Programming
- Generators
- Decorators
- File Handling
- Exception Handling
- Command-line Interface

## Author

Mustafa Bekirov

---

*Part of the GoIT Python Core learning program.*
