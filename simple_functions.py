def double_number(a):
    """
    Double the value of the input number.

    Args:
        a (int or float): The number to be doubled.

    Returns:
        int or float: The result of doubling the input number.

    Example:
        double_number(5)
        10
    """
    print(f"value before double_number(): {a}")
    result = a + a
    print(f"value after double_number(): {result}")
    return result


def square_number(a):
    """
    Calculate the square of the input number.

    Args:
        a (int or float): The number to be squared.

    Returns:
        int or float: The square of the input number.

    Example:
        square_number(4)
        16
    """
    print(f"value before square_number(): {a}")
    result = a * a
    print(f"value after square_number(): {result}")
    return result
