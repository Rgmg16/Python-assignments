# 1. Match a word boundary
import re
text = "This is a word boundary example. Match the word 'word'."
matches = re.findall(r'\bword\b', text)
print(matches)  # Output: ['word']

# 2. Regex to match a date DD/MM/YYYY:

text = "Today's date is 05/29/2024 and tomorrow's date is 05/30/2024"
matches = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print(matches)  # Output: ['05/29/2024', '05/30/2024']

# 3. Regex to match a URL

text = "Visit our website at https://www.example.com or check out our blog at http://blog.example.com"
urls = re.findall(r'https?://\S+', text)
print(urls)  # Output: ['https://www.example.com', 'http://blog.example.com']

# 4. Regex to match an email address

text = "Contact us at info@example.com or support@example.net"
email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(email_addresses)  # Output: ['info@example.com', 'support@example.net']

# 5.Regex to match a Kenyan phone number

text = "Contact us at 0712345678 or 0723456789 for assistance."
phone_numbers = re.findall(r'07\d{8}', text)
print(phone_numbers)  # Output: ['0712345678', '0723456789']
