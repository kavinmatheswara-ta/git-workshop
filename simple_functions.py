# Custom python functions

def double_number(a):
    return a+a
def square_number(a):
    return a*a


a = 5
print(f'value before double_number(): {a}')
result = double_number(a)
print(f'value after double_number(): {result}')

print(f'value before square_number(): {a}')
result = square_number(a)
print(f'value after square_number(): {result}')
