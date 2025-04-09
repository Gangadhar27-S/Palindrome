import pytest
from palindrome import is_palindrome  # Adjust the import based on your project structure

# Test for palindrome with an even length string
def test_palindrome_even_length(capfd):
    is_palindrome("abba")  # Should print "Palindrome"
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Palindrome"  # Verify the printed output is "Palindrome"

# Test for palindrome with an odd length string
def test_palindrome_odd_length(capfd):
    is_palindrome("madam")  # Should print "Palindrome"
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Palindrome"  # Verify the printed output is "Palindrome"

# Test for a string that is not a palindrome
def test_not_palindrome(capfd):
    is_palindrome("hello")  # Should print "Not a palindrome"
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Not a palindrome"  # Verify the printed output is "Not a palindrome"

# Test for an empty string, which is trivially a palindrome
def test_empty_string(capfd):
    is_palindrome("")  # Should print "Palindrome"
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Palindrome"  # Verify the printed output is "Palindrome"

# Test for a single character string, which is trivially a palindrome
def test_single_character(capfd):
    is_palindrome("a")  # Should print "Palindrome"
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Palindrome"  # Verify the printed output is "Palindrome"

# Test for a string with mixed case (e.g., "MadAm") — Should not be a palindrome without case-insensitive check
def test_mixed_case(capfd):
    is_palindrome("MadAm")  # Should print "Not a palindrome" unless the function is made case-insensitive
    captured = capfd.readouterr()  # Capture the output
    out, err = captured
    assert out.strip() == "Not a palindrome"  # Verify the printed output is "Not a palindrome"
