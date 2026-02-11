# Ralph Wiggum Fun App

A delightful Python CLI application featuring Ralph Wiggum from The Simpsons! Enjoy random Ralph quotes and help him with his math homework.

## Overview

The Ralph Wiggum Fun App is a menu-driven command-line application that brings Ralph's innocent humor to your terminal. Choose between viewing random Ralph Wiggum quotes or helping Ralph solve simple addition problems (with hilarious results when the math gets too hard!).

## Features

### 1. Random Quote Display
- Displays authentic Ralph Wiggum quotes from The Simpsons
- 8 memorable quotes featuring Ralph's unique perspective
- Each execution shows a different random quote

### 2. Math Homework Helper
- Help Ralph solve addition problems
- **Easy problems** (sum ≤ 10): Ralph counts on his fingers and gives you the answer!
- **Hard problems** (sum > 10): Ralph runs out of fingers and gets confused
- All responses maintain Ralph's endearing character voice

### 3. User-Friendly Interface
- Simple menu-driven navigation
- Graceful error handling with Ralph-style messages
- Keyboard interrupt (Ctrl+C) handled gracefully

## Requirements

- **Python**: 3.8 or higher
- **Dependencies**: None (uses only Python standard library)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## Installation

No installation required! Simply download the files and run.

1. Download or clone the repository:
   ```bash
   git clone <repository-url>
   cd ralph_wiggum_app
   ```

2. Ensure you have Python 3.8+ installed:
   ```bash
   python3 --version
   ```

## Usage

### Running the Application

```bash
python3 ralph_app.py
```

Or on Windows:
```bash
python ralph_app.py
```

### Menu Options

When you run the application, you'll see:

```
=================================
  Ralph Wiggum Fun App!
=================================

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3):
```

**Option 1**: Displays a random Ralph Wiggum quote
**Option 2**: Interactive math homework helper
**Option 3**: Exit the application

## Example Interactions

### Viewing a Quote

```
Choose an option (1-3): 1

==================================================
Ralph Wiggum says:
"Me fail English? That's unpossible!"
==================================================
```

### Easy Math Problem (sum ≤ 10)

```
Choose an option (1-3): 2

Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: 3
Second number: 4

Ralph is trying to solve: 3.0 + 4.0
Ralph is thinking really hard...

==================================================
I counted on my fingers! The answer is 7.0! I'm learnding!
==================================================
```

### Hard Math Problem (sum > 10)

```
Choose an option (1-3): 2

Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: 15
Second number: 20

Ralph is trying to solve: 15.0 + 20.0
Ralph is thinking really hard...

==================================================
That's too hard! I ran out of fingers! My brain hurts!
==================================================
```

## File Structure

```
ralph_wiggum_app/
├── ralph_app.py          # Main application and menu system
├── quotes.py             # Quote storage and selection
├── math_helper.py        # Math homework helper logic
├── README.md             # This file
└── requirements.txt      # Empty (no external dependencies)
```

## Features in Detail

### Quote System
- 8 authentic Ralph Wiggum quotes from The Simpsons
- Random selection using Python's `random.choice()`
- Formatted display with decorative borders
- Instant execution (< 100ms)

### Math Helper
- Accepts any numeric input (integers, decimals, negative numbers)
- Difficulty threshold: sum ≤ 10 (easy) vs sum > 10 (hard)
- Easy problems: Shows correct answer with encouraging message
- Hard problems: Shows humorous "too hard" message without answer
- Input validation with retry logic
- All responses in Ralph's character voice

### Error Handling
- Invalid menu choices: Friendly error messages with retry
- Invalid numeric input: Ralph-style error messages with retry
- Keyboard interrupt (Ctrl+C): Graceful exit with goodbye message
- Unexpected errors: Caught and handled without crashes

## Character Voice

All messages maintain Ralph Wiggum's innocent, endearing personality:
- "I'm learnding!"
- "That's unpossible!"
- "My brain hurts!"
- "I counted on my fingers!"

## Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed: `python3 --version`
- Check that all three Python files are in the same directory
- Try: `python3 ralph_app.py` instead of `python ralph_app.py`

### Import errors
- Verify `quotes.py` and `math_helper.py` are in the same directory as `ralph_app.py`
- Check file permissions (files should be readable)

### Math helper not accepting input
- Ensure you're entering numeric values only
- Use decimal point for decimals (e.g., `3.14` not `3,14`)
- Negative numbers are supported (e.g., `-5`)

## Technical Details

- **Language**: Python 3.8+
- **Architecture**: Modular design with three main components
- **Dependencies**: Standard library only (`random`, `sys`)
- **Performance**: < 1 second startup, < 100ms feature execution
- **Memory**: < 10MB footprint
- **Style**: PEP 8 compliant

## Credits

- **Application**: IBM Bob
- **Character**: Ralph Wiggum from The Simpsons (created by Matt Groening)
- **Version**: 1.0
- **Date**: February 11, 2026

## License

This is a fan project for educational and entertainment purposes. Ralph Wiggum and The Simpsons are property of their respective copyright holders.

## Version History

### Version 1.0 (February 11, 2026)
- Initial release
- 8 Ralph Wiggum quotes
- Math homework helper with difficulty threshold
- Menu-driven CLI interface
- Comprehensive error handling
- Full PEP 8 compliance

---

**"I'm learnding!"** - Ralph Wiggum
