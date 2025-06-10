import pytest
from app.operations import Operations


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-2, -3, -5),
    (-1, 0, -1),
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-2, -3, -5),
    (-1, 0, -1),
], ids=[
    "add_two_positive_integers",
    "add_two_zeros",
    "add_negative_and_positive",
    "add_two_negative_integers",
    "add_negative_and_zero",
])
def test_addition(a, b, expected):
    # The test cases cover a range of scenarios, including adding two positive integers,
    # adding two zeros, adding a negative and a positive integer, and adding two negative integers.
    # Each test case is identified by a unique ID for clarity.
    # The expected results are provided for each case, and the assertion checks if the addition operation
    # produces the correct result.
        
    assert Operations.addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (10, 5, 5),
    (-5, -3, -2),
    (3, 5, -2),
], ids=[
    "subtract_smaller_from_larger",
    "subtract_zeros",
    "subtract_half_value",
    "subtract_two_negatives",
    "subtract_larger_from_smaller",
])
def test_subtraction(a, b, expected):
    #This function tests the subtraction operation with various pairs of integers
    # It checks both positive and negative results, including zero. 
    # Each test case is identified by a unique ID for clarity.
    # The expected results are provided for each case, and the assertion checks if the subtraction operation
    # produces the correct result.
    assert Operations.subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 10, 0),
    (-2, -3, 6),
    (2, -3, -6),
    (-2, 3, -6),
], ids=[
    "multiply_two_positives",
    "multiply_zero_and_positive",
    "multiply_two_negatives",
    "multiply_positive_and_negative",
    "multiply_negative_and_positive",
])
def test_multiplication(a, b, expected):
    # This function tests the multiplication operation with various pairs of integers.
    # It checks both positive and negative results, including zero.
    # Each test case is identified by a unique ID for clarity.
    # The expected results are provided for each case, and the assertion checks if the multiplication operation
    # produces the correct result.

    assert Operations.multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (-6, -3, 2.0),
    (6.0, 3.0, 2.0),
    (-6.0, 3.0, -2.0),
    (0, 5, 0.0),
], ids=[
    "divide_two_positive_integers",
    "divide_two_negative_integers",
    "divide_two_positive_floats",
    "divide_negative_float_by_positive_float",
    "divide_zero_by_positive_integer",
])
def test_division(a, b, expected):
    # This function tests the division operation with various pairs of integers and floats.
    # It checks both positive and negative results, including zero.
    # Each test case is identified by a unique ID for clarity.
    # The expected results are provided for each case, and the assertion checks if the division operation
    # produces the correct result.
    # The expected results are provided for each case, and the assertion checks if the division operation
    # produces the correct result.
    # Note: Division by zero is handled separately in another test function.
    assert Operations.division(a, b) == expected


@pytest.mark.parametrize("a, b", [
    (1, 0),
    (-5, 0),
    (0, 0),
], ids=[
    "divide_positive_by_zero",
    "divide_negative_by_zero",
    "divide_zero_by_zero",
])
def test_division_by_zero(a, b):
    # This function tests the division operation with a zero denominator.
    # It checks that a ValueError is raised when attempting to divide by zero.
    # Each test case is identified by a unique ID for clarity.
    # The test cases cover dividing a positive integer by zero, dividing a negative integer by zero,
    # and dividing zero by zero.
    # The expected behavior is that a ValueError is raised with a specific message. 
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(a, b)
