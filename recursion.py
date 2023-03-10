"""
recursion.py file!
"""

def countdoun(i):
    print(i)
    if i <= 0: # Базовый случай!
        return
    else:      # Рекурсивный случай!
        countdoun(i-1)

def greet(name):
    print(f"Hello {name} !")
    greet2(name)
    print("getting ready to say bay...")
    bye()

def greet2(name):
    print(f"How are you, {name} ?")

def bye():
    print("Ok bye!")


print(greet("Ivan"))

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))