# palindrome check

text = "abcd"
# python slicing
# string[start : stop : step]
reverse_text = text[::-1]

if text == reverse_text:
    print("It's a palindrome")
else:
    print("It's not a palindrome")