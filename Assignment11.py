# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

def contains_only_allowed_characters(s):
    # Define the regular expression pattern
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    
    # Check if the string matches the pattern
    if pattern.match(s):
        return True
    else:
        return False

# Test cases
test_string1 = "HelloWorld123"
test_string2 = "Hello World!"
test_string3 = "1234567890"
test_string4 = "hello_world"

print(f"'{test_string1}' contains only a-z, A-Z, and 0-9: {contains_only_allowed_characters(test_string1)}")
print(f"'{test_string2}' contains only a-z, A-Z, and 0-9: {contains_only_allowed_characters(test_string2)}")
print(f"'{test_string3}' contains only a-z, A-Z, and 0-9: {contains_only_allowed_characters(test_string3)}")
print(f"'{test_string4}' contains only a-z, A-Z, and 0-9: {contains_only_allowed_characters(test_string4)}")


# 2.Write a Python program that matches a string that has an ‘a’ followed by anything, ending in ‘b’.
import re

def match_pattern(s):
    # Define the regular expression pattern
    pattern = re.compile(r'^a.*b$')
    
    # Check if the string matches the pattern
    if pattern.match(s):
        return True
    else:
        return False

# Test cases
test_string1 = "a123b"
test_string2 = "ab"
test_string3 = "aXYZb"
test_string4 = "abc"
test_string5 = "bac"
test_string6 = "a_b"

print(f"'{test_string1}' matches the pattern: {match_pattern(test_string1)}")
print(f"'{test_string2}' matches the pattern: {match_pattern(test_string2)}")
print(f"'{test_string3}' matches the pattern: {match_pattern(test_string3)}")
print(f"'{test_string4}' matches the pattern: {match_pattern(test_string4)}")
print(f"'{test_string5}' matches the pattern: {match_pattern(test_string5)}")
print(f"'{test_string6}' matches the pattern: {match_pattern(test_string6)}")

# 3.Write a program that uses regex to validate user input. Examples:
# Check if a password meets certain criteria (e.g., minimum length, containing uppercase and lowercase letters).
# Validate a date format (e.g., DD/MM/YYYY).

import re

def validate_password(password):
    # Define the regular expression pattern
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$')
    
    # Check if the password matches the pattern
    if pattern.match(password):
        return True
    else:
        return False

# Test cases
passwords = ["Password123", "password", "PASSWORD", "Pass123", "PassworD1"]

for pwd in passwords:
    print(f"Password: {pwd}, Valid: {validate_password(pwd)}")

import re

def validate_date(date):
    # Define the regular expression pattern
    pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$')
    
    # Check if the date matches the pattern
    if pattern.match(date):
        return True
    else:
        return False

# Test cases
dates = ["01/01/2020", "31/12/1999", "30/02/2020", "29/02/2020", "32/01/2020", "12/13/2020"]

for date in dates:
    print(f"Date: {date}, Valid: {validate_date(date)}")

# 4. Write a program that uses regex to extract specific information from a string. Examples:
# Extract email addresses: Find all strings containing “@” and a dot (.).
# Extract phone numbers: Find all strings with a specific format (e.g., XXX-XXX-XXXX).

import re

def extract_emails(text):
    # Define the regular expression pattern for email addresses
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    # Find all matching email addresses in the text
    emails = pattern.findall(text)
    return emails

# Test string
text = """
Hello, you can reach out to john.doe@example.com for more information.
Alternatively, contact jane_doe123@domain.co.uk or support@company.com.
"""

# Extract emails
emails = extract_emails(text)

# Print the extracted emails
print("Extracted emails:")
for email in emails:
    print(email)

import re

def extract_phone_numbers(text):
    # Define the regular expression pattern for phone numbers
    pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
    
    # Find all matching phone numbers in the text
    phone_numbers = pattern.findall(text)
    return phone_numbers

# Test string
text = """
You can contact us at 123-456-7890 or 987-654-3210.
Our old number 111-222-3333 is no longer in service.
"""

# Extract phone numbers
phone_numbers = extract_phone_numbers(text)

# Print the extracted phone numbers
print("Extracted phone numbers:")
for number in phone_numbers:
    print(number)


# 5. Write a program that uses regex to search for and replace text in a string. Example:
# Replace all occurrences of “Mr.” with “Ms.”: text.replace(r”Mr.”, “Ms.”) (r prefix for raw string)

import re

def replace_text(text, pattern, replacement):
    # Use re.sub() to perform the replacement
    new_text = re.sub(pattern, replacement, text)
    return new_text

# Test string
text = "Mr. John Doe and Mr. Smith went to see Mr. Brown."

# Define the pattern to search for
pattern = r"Mr\."

# Define the replacement string
replacement = "Ms."

# Perform the replacement
new_text = replace_text(text, pattern, replacement)

# Print the original and modified text
print("Original text:", text)
print("Modified text:", new_text)
