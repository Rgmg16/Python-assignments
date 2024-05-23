def is_palindrome(input_string):
 return input_string == input_string[::-1]
input_string = "madam"
print("Is Palindrome:", is_palindrome(input_string))