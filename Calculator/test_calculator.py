from calculator import divide_numbers,add_numbers


# Method 1: Simple assertions (Basic approach)
def test_add_numbers():
    # Test normal case
    result = add_numbers(5, 3)
    assert result == 8, f"Expected 8, but got {result}"
    
    # Test with negative numbers
    result = add_numbers(-2, 3)
    assert result == 1, f"Expected 1, but got {result}"
    
    # Test with zero
    result = add_numbers(0, 5)
    assert result == 5, f"Expected 5, but got {result}"
    
    print("All addition tests passed!")

def test_divide_numbers():
    # Test normal division
    result = divide_numbers(10, 2)
    assert result == 5, f"Expected 5, but got {result}"
    
    # Test division resulting in decimal
    result = divide_numbers(7, 2)
    assert result == 3.5, f"Expected 3.5, but got {result}"
    
    # Test division by zero (should raise an error)
    try:
        divide_numbers(5, 0)
        assert False, "Expected ValueError but no error was raised"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    
    print("All division tests passed!")

# Run the tests
if __name__ == "__main__":
    test_add_numbers()
    test_divide_numbers()
    print("All tests completed successfully!")
