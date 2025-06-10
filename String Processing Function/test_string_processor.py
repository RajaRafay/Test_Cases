from string_processor import format_name,count_words

def test_format_name():
    # Test normal case
    result = format_name("john", "doe")
    assert result == "John Doe"
    
    # Test with extra spaces
    result = format_name("  jane  ", "  smith  ")
    assert result == "Jane Smith"
    
    # Test with mixed case
    result = format_name("aLiCe", "jOhNsOn")
    assert result == "Alice Johnson"
    
    # Test with empty first name
    result = format_name("", "Brown")
    assert result == "Invalid name"
    
    # Test with empty last name
    result = format_name("Bob", "")
    assert result == "Invalid name"
    
    print("Name formatting tests passed!")

def test_count_words():
    # Test normal sentence
    result = count_words("Hello world")
    assert result == 2
    
    # Test single word
    result = count_words("Python")
    assert result == 1
    
    # Test empty string
    result = count_words("")
    assert result == 0
    
    # Test string with only spaces
    result = count_words("   ")
    assert result == 0
    
    # Test sentence with extra spaces
    result = count_words("  This   has   extra   spaces  ")
    assert result == 4
    
    print("Word counting tests passed!")

# Run tests
if __name__ == "__main__":
    test_format_name()
    test_count_words()
    print("All string processing tests completed!")

