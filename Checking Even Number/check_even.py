def is_even(number):
    """Return True if number is even, False otherwise"""
    if not number:
        return 'No number exists'
    if number < 0:
        return 'Negative number'
    return True if number % 2 == 0 else False
