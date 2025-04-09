import pytest
from palindrome import is_palindrome  # Assuming the function is saved in `palindrome.py`

@pytest.mark.parametrize("test_input, expected", [
    ("racecar", True),
    ("madam", True),
    ("hello", False),
    ("", True),  # An empty string is considered a palindrome
    ("A man a plan a canal Panama", False),  # Case-sensitive and space-sensitive check
])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected

if __name__ == "__main__":
    pytest.main()
