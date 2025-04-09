def is_palindrome(string):
   reversed_string=""
   # transversing through string from last
   for i in range(len(string),0,-1):
      # Addind last characters of string into a new string
      reversed_string+=string[i-1]
      if string==reversed_string:
         print("Palindrome")
      else:
         print("Not a palindrome")
