s = "malayalam"  # string

i,j = 0, len(s) - 1  # two pointers

is_Palindrome = True  # assume palindrome
while i < j:
    if s[i] != s[j]:  # mismatch found
        is_Palindrome = False
        break
    i += 1
    j -= 1

if is_Palindrome:
    print("Yes") 
else:
    print("No")  
