class Calculator:
    _instance = None

    def __new__(cls):
        # Singleton design pattern: Ensures only one instance of Calculator is created
        if cls._instance is None:
            cls._instance = super(Calculator, cls).__new__(cls)
            # Private variables for internal use
            cls._instance._output_queue = []
            cls._instance._operator_stack = []
        return cls._instance

    def _get_precedence(self, operator):
        # Returns the precedence of operators for Shunting Yard(SY) algorithm
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        return precedence.get(operator, 0)

    def _shunting_yard(self, expression):
        # SY algorithm for converting infix expression to Reverse Polish Notation (RPN)
        for token in expression:
            if token.isdigit() or '.' in token:
                # Operand: add to output queue
                self._output_queue.append(float(token))
            elif token in {"+", "-", "*", "/"}:#more operations can be added here
                # Operator: handle operator precedence and stack operations
                while (self._operator_stack and
                       self._get_precedence(self._operator_stack[-1]) >= self._get_precedence(token)):
                    self._output_queue.append(self._operator_stack.pop())
                self._operator_stack.append(token)
            elif token == "(":
                # Left parenthesis: push onto the stack
                self._operator_stack.append(token)
            elif token == ")":
                # Right parenthesis: pop operators from the stack to output until left parenthesis is reached
                while self._operator_stack and self._operator_stack[-1] != "(":
                    self._output_queue.append(self._operator_stack.pop())
                self._operator_stack.pop()

        # Pop any remaining operators from the stack to output
        while self._operator_stack:
            self._output_queue.append(self._operator_stack.pop())

    def evaluate_expression(self, expression):
        # Evaluate the expression using SY and stack-based evaluation
        self._output_queue = []
        self._operator_stack = []

        expression = self._tokenize_expression(expression)
        self._shunting_yard(expression)

        stack = []
        for token in self._output_queue:
            if isinstance(token, float):
                # Operand: push onto the stack
                stack.append(token)
            elif token in {"+", "-", "*", "/"}:
                # Operator: pop operands, perform operation, and push result onto the stack
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(self.add_numbers(a, b))
                elif token == "-":
                    stack.append(self.subtract_numbers(a, b))
                elif token == "*":
                    stack.append(self.multiply_numbers(a, b))
                elif token == "/":
                    stack.append(self.divide_numbers(a, b))

        # Result is the only item on the stack
        return stack[0] if stack else 0

    def _tokenize_expression(self, expression):
        # Tokenize the input expression
        tokens = []
        current_token = ""

        for char in expression:
            if char.isdigit() or char == '.':
                # Accumulate digits for operand
                current_token += char
            elif char in {"+", "-", "*", "/", "(", ")"}:
                if current_token:
                    # Add accumulated operand to tokens
                    tokens.append(current_token)
                    current_token = ""
                # Add operator or parenthesis to tokens
                tokens.append(char)

        # Add any remaining operand to tokens
        if current_token:
            tokens.append(current_token)

        return tokens

    @staticmethod
    def add_numbers(a, b):
        # Static method for addition
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        # Static method for subtraction
        return a - b

    @staticmethod
    def multiply_numbers(a, b):
        # Static method for multiplication
        return a * b

    @staticmethod
    def divide_numbers(a, b):
        # Static method for division with error handling
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero.")
            #return 0
            exit()


if __name__ == "__main__":
    # Entry point of the script
    calculator = Calculator()

    while True:
        try:
            choice = input("Enter 'expr' to evaluate an expression, 'op' for direct operation, or 'exit' to quit: ")

            if choice.lower() == 'exit':
                break
            elif choice.lower() == 'expr':
                expression = input("Enter the expression: ")
                result = calculator.evaluate_expression(expression)
                print(f"Result: {result}")
            elif choice.lower() == 'op':
                operation = input("Enter the operation (add/subtract/multiply/divide): ")
                if operation.lower()!=["add","subtract","multiply","divide"]:
                    print("Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")
                else:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))

                    result = 0
                    if operation.lower() == 'add':
                        result = calculator.add_numbers(num1, num2)
                    elif operation.lower() == 'subtract':
                        result = calculator.subtract_numbers(num1, num2)
                    elif operation.lower() == 'multiply':
                        result = calculator.multiply_numbers(num1, num2)
                    elif operation.lower() == 'divide':
                        result = calculator.divide_numbers(num1, num2)
                    else:
                        print("Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")

                    print(f"Result: {result}")

                    more_numbers = input("Do you want to enter more numbers? (yes/no): ")
                    while more_numbers.lower() == 'yes':
                        # Ask for a new operation and number
                        operation = input("Enter the operation (add/subtract/multiply/divide): ")
                        additional_num = float(input("Enter the next number: "))
                        if operation.lower() == 'add':
                            result = calculator.add_numbers(result, additional_num)
                        elif operation.lower() == 'subtract':
                            result = calculator.subtract_numbers(result, additional_num)
                        elif operation.lower() == 'multiply':
                            result = calculator.multiply_numbers(result, additional_num)
                        elif operation.lower() == 'divide':
                            result = calculator.divide_numbers(result, additional_num)
                        else:
                            print("Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")
                            break

                        print(f"Result: {result}")
                        more_numbers = input("Do you want to enter more numbers? (yes/no): ")

            else:
                print("Invalid choice. Please enter 'expr', 'op', or 'exit'.")

        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")
