"""
hello_admin.py file!
"""

current_users = ["Ivan", "Alice", "Bob", "Alex", "Sue", "Admin"]
new_users = ["IVAN", "Alice", "Edvard", "Stive", "Oleg", "Kenny"]

for i in new_users:
    if i.title() in current_users:
        print(f"User_name is {i} ivalid")
    else:
        print(f"Your user_ name {i} is correct!")