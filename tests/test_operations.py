import pytest
from app.operations import Operations


@pytest.mark.parametrize("a, b, expected", [
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
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(a, b)
