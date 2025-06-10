class Operations:
    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their sum (a + b).
        It expects both inputs to be numeric and will return their total as a float.
        Example: Operations.addition(2.0, 3.0) will return 5.0.
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their difference (a - b).
        It expects two numeric values and subtracts b from a.
        Example: Operations.subtraction(10.0, 4.0) will return 6.0.
        """
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        This static method multiplies two numbers (a and b) and returns the result (a * b).
        It is useful for scaling values or computing repeated addition.
        Example: Operations.multiplication(3.0, 4.0) will return 12.0.
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        This static method divides one number (a) by another (b) and returns the result (a / b).
        If b is zero, it raises a ValueError to prevent division by zero.
        Example: Operations.division(8.0, 2.0) will return 4.0.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
