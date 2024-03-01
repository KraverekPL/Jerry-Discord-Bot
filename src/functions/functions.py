def fibonacci_sequence(number):  # write fibonacci sequence up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = ''
    while a < number:
        result = result + ' ' + str(a)
        a, b = b, a + b
    return result
