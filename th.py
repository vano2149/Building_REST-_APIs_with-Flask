"""
th.py file!
"""

def quicksort(array:list)->list:
    """
    Быстрая сортировка!
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

#if __name__ == "__main__":
#   print(quicksort([10,5,2,3,7]))



# Бинарный поиск без цикла ! 

def binary_search(arr:list, low:int, high:int, x:int)-> int:

    # Проверяем базовый случай!
    if high >= low:
        mid = (high + low) // 2
        # Если мы попали в элемент!
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

#if __name__ == "__main__":
#    arr = [2,3,4,5,10,40]
#    x = 2
#    print(binary_search(arr, 0, len(arr)-1, x))

def binary_search_with_while(arr:list, x:int)->int:
    """
    """
    low = 0
    high = len(arr) -1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return -1


#if __name__ == "__main__":
    #print("-" * 10) # 5 -> 10
    #arr = [1,2,3,4,5,10,40]
    #print(binary_search_with_while(arr, 10))


def quick_sort1(arr:list)->list:
    """
    Fast sorted!
    """
    if len(arr) < 2:
        return arr
    else:
        pivod = arr[0]
        less = [i for i in arr[1:] if i <= pivod]
        greater = [i for i in arr[1:] if i > pivod]
    return quick_sort1(less) + [pivod] + quick_sort1(greater)

#if __name__ == "__main__":
    #print(quick_sort1([10,5,2,3,7]))

def bin_search(array:list, target:int)-> int:
    """
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)
        if array[mid] == target:
            return mid
        if array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

#if __name__ == "__main__":
    #print(bin_search([1,2,3,4,5,10,40], 40))


def fast_sort(array:list) -> list:
    """
    This func releace a fast sorted!
    """
    if len(array) < 2:
        return array
    else:
        pivod = array[0]
        less = [i for i in array[1:] if i <= pivod]
        greater = [i for i in array[1:] if i > pivod]
    return fast_sort(less) + [pivod] + fast_sort(greater)


#if __name__ == "__main__":
    #print(fast_sorted([5, 8, 2, 6, 10, 32, 23]))


def table_sqrt(array:list) -> list:
    """
    """
    new_array = []
    for i in range(len(array)):
        con = []
        for j in range(len(array)):
            con.append(array[i] * array[j])
        new_array.append(con)
    return new_array
#if __name__ == "__main__":
    #print(table_sqrt([2,3,7,8,10]))
# страница 99-100!


from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        """
        count = 0
        l= []
        for i in nums:
            count += i
            l.append(count)
        return l
if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1,2,3,4]))

