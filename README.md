# Arithmetic Problem Formatter

## Overview
The **Arithmetic Problem Formatter** is a Python function that arranges and optionally solves simple arithmetic problems (addition and subtraction). This project ensures that problems are neatly formatted and aligned for better readability, making it useful for educational purposes.

## Features
- Accepts up to **five** arithmetic problems.
- Supports **addition** (`+`) and **subtraction** (`-`).
- Ensures numbers are **no longer than four digits**.
- Arranges problems neatly in columns.
- Optionally displays the answers when requested.
- Provides error messages for incorrect input formats.

## Usage
Import the function and call it with a list of arithmetic problems:

```python
from arithmetic_formatter import arrange_arithmetic_problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted_output = arrange_arithmetic_problems(problems, show_answers=True)
print(formatted_output)
```

## Output Example
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

## Error Handling
The function will return an error message for the following cases:
- More than five problems: `"Error: Too many problems."`
- Invalid operators: `"Error: Operator must be '+' or '-'"`
- Non-numeric inputs: `"Error: Numbers must only contain digits."`
- Numbers longer than four digits: `"Error: Numbers cannot be more than four digits."`

## Installation
No additional dependencies are required. Just copy the function into your Python script and use it as needed.

## License
This project is released under the MIT License.

