"""
binary_search.py file!
"""

def binary_search(list1, item):
    """
    В переманных low и high хранятся границы
    той части спискаб в которой выполняется
    поиск.
    """
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high)
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None
if __name__ == "__main__":
    print(binary_search([1,3,5,7,9], 3))


#256 / 2 = 128
#128 / 2 = 64
# 64 / 2 = 32
# 32 / 2 = 16
# 16 / 2 = 8
# 8 / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# Ответ = 52