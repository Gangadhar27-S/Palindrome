import pytest
from palindrome import is_palindrome

def test_palindrome_even_length(capfd):
    is_palindrome("abba")
    captured = capfd.readouterr()
    out, err = captured
    assert out.strip().endswith("Palindrome")  # Ensure the last output is "Palindrome"

def test_palindrome_odd_length(capfd):
    is_palindrome("madam")
    captured = capfd.readouterr()
    out, err = captured
    assert out.strip().endswith("Palindrome")  # Ensure the last output is "Palindrome"

def test_not_palindrome(capfd):
    is_palindrome("hello")
    captured = capfd.readouterr()
    out, err = captured
    assert out.strip().endswith("Not a palindrome")  # Ensure the last output is "Not a palindrome"

def test_mixed_case(capfd):
    is_palindrome("MadAm")  # Should print "Not a palindrome" unless the function is case-insensitive
    captured = capfd.readouterr()
    out, err = captured
    assert out.strip().endswith("Not a palindrome")  # Ensure the last output is "Not a palindrome"
