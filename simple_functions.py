# Custom python functions

def double_number(a):
    """A function to double a given number."""
    print(f'value before double_number(): {a}')
    result = a+a
    print(f'value after double_number(): {result}')
    return result

def square_number(a):
    """A function to square a given number."""
    print(f'value before square_number(): {a}')
    result = a*a
    print(f'value after square_number(): {result}')
    return result