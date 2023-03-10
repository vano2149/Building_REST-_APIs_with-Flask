"""
look_for_key.py file!
"""
"""
def look_for_key(main_box):
    '''
    Пока куча коробок не пуста возьми очередную коробку!
    '''
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!!!")

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) # Рекурсия !!!
        elif item.is_a_key():
            print("Found the key!!!!")
"""
"""
def countdown(item):
    print(item)
    if item <= 0: # Базовый случай.
        return
    else:
        countdown(item - 1) # Рекурсивный случай!

countdown(12)
"""

"""
def greet(name):
    print(f"Hello {name} !")
    greet2(name)
    print(f"getting ready to say bye...")
    bye()

def greet2(name):
    print(f"How are you, {name} ?")

def bye():
    print("ok bye!")



greet("maggie")
"""

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x -1)

print(fact(3))