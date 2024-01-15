# Calculator

## Overview

This Python program implements a basic calculator that allows users to evaluate mathematical expressions and perform direct arithmetic operations. The calculator supports addition, subtraction, multiplication, and division.

## Features

- Arithmetic operations: Addition, subtraction, multiplication, and division.
- Expression evaluation: Users can input mathematical expressions for evaluation.
- Shunting Yard algorithm: Converts infix expressions to Reverse Polish Notation (RPN) for evaluation.

## Usage

1. Run the `calculator.py` script.
2. Choose one of the following options:
   - `expr`: Evaluate a mathematical expression.
   - `op`: Perform a direct arithmetic operation.
   - `exit`: Quit the calculator.

### Expression Evaluation (`expr`)

- Enter a mathematical expression when prompted.
- The calculator will evaluate the expression and display the result.

### Direct Operation (`op`)

- Choose an operation: add, subtract, multiply, or divide.
- More operations can be added
- Enter two numbers to perform the chosen operation.
- Optionally, enter more numbers and operations if desired.

### Termination

- To exit the calculator, enter `exit` when prompted for the choice.

## Error Handling

- The program handles invalid input and provides appropriate error messages.
- Division by zero is explicitly handled to prevent runtime errors.
