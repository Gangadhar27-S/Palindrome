def is_palindrome(string):
    reversed_string = ""
    # Traverse through string in reverse order
    for i in range(len(string), 0, -1):
        reversed_string += string[i - 1]
    
    # Check if the original string is equal to the reversed string
    if string == reversed_string:
        print("Palindrome")
    else:
        print("Not a palindrome")
