import pytest
from palindrome import is_palindrome  # Adjust the import based on your project structure

def test_palindrome_even_length():
    # Test an even-length palindrome string
    captured = capfd.readouterr()  # Capture the output
    is_palindrome("abba")  # Should print "Palindrome"
    out, err = captured
    assert out.strip() == "Palindrome"

def test_palindrome_odd_length():
    # Test an odd-length palindrome string
    captured = capfd.readouterr()  # Capture the output
    is_palindrome("madam")  # Should print "Palindrome"
    out, err = captured
    assert out.strip() == "Palindrome"

def test_not_palindrome():
    # Test a string that is not a palindrome
    captured = capfd.readouterr()  # Capture the output
    is_palindrome("hello")  # Should print "Not a palindrome"
    out, err = captured
    assert out.strip() == "Not a palindrome"

def test_empty_string():
    # Test an empty string, which is trivially a palindrome
    captured = capfd.readouterr()  # Capture the output
    is_palindrome("")  # Should print "Palindrome"
    out, err = captured
    assert out.strip() == "Palindrome"

def test_single_character():
    # Test a single-character string, which is trivially a palindrome
    captured = capfd.readouterr()  # Capture the output
    is_palindrome("a")  # Should print "Palindrome"
    out, err = captured
    assert out.strip() == "Palindrome"
