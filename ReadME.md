# FreeCodeCamp - Arithmetic Formatter

This is my Python project developed as part of a practice exercise for [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project). The goal of this project is to use python to implement a function that formats arithmetic problems in a specific way.

## Features

- Formats basic arithmetic problems (addition and subtraction).
- Supports multiple problems arranged in a visually pleasing way.
- Provides an option to display the solutions to the problems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Installation

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/CMartin0-0/Practice-Project--FreeCodeCamp_Arithmetic_Formatter.git
   ```
2. Ensure you have Python installed (version 3.6 or later).
3. Navigate to the project folder:
   ```bash
   cd Practice-Project--FreeCodeCamp_Arithmetic_Formatter
   ```

## Usage

1. Import the `arithmetic_arranger` function into your Python script or interactive environment:
   ```python
   from arithmetic_formatter import arithmetic_arranger
   ```
2. Pass a list of arithmetic problems to the function to format them:
   ```python
   print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], solve=True))
   ```

## Examples

### Input
```python
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(problems, solve=True)
```

### Output
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to submit a pull request. Before contributing, please ensure your code adheres to Python's best practices and is well-tested.

--- 

Feel free to reach out with any questions or feedback!
