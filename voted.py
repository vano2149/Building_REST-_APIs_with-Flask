"""
voted.py file!
"""

voted = {}
def check_voted(name:str)->None:
    """
    Проверка на вхождение в Dict.
    """
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print("let them vote!")

# стр 116.