"""
color.py file!
"""


# Создайте список из 5-ти или более имен пользователей!
user_name = ["Ivan", "Alice", "Bob", "Alex", "Sue", "Admin"]

for i in user_name:
    if i.lower() == 'admin':
        print(f"Hello {i}, would you like to see ststus report?")
    else:
        print(f"Hello {i}, thank you for logging in again!")
