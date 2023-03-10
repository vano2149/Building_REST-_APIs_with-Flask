"""
fast_sort.py file!
Быстрая сортировка !!!
Принцип разделяй и властвуй! )) 
"""

def sum1(arr):
    """
    Имеется масив чисел 246!
    """
    total = 0
    for x in arr:
        total += x
    return total +1

#print(sum1([1, 2, 3, 4]))


def counts(arr):
    """
    Фун-ция считает кол-во элементов в списке.
    """
    count = 0 # счетчик
    for i in arr: # бегаем циклом по списку 
        count += 1 # плюсуем каждую итерацию
    return count # Возвращаем кол-во элементов.



def higth_value(arr:list)->int:
    max1 = arr[0]
    for i in arr:
        if i > max1:
            max1 = i
    return max1


def quicsort(array:list) -> list:
    if len(array) <2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1::] if i <= pivot]
        greater = [i for i in array[1::] if i > pivot]
        return quicsort(less) + [pivot] + quicsort(greater)


# Глава 4. стр. 86

# Быстрая сортировка.
def quick_sort(array:list)->list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        gretter = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(gretter)


# Сортировка слиянием!
def print_items(list1):
    for item in list1:
        print(item)


from time import sleep

def print_items2(list1):
    for item in list1:
        print(item)
        sleep(1)

if __name__ == "__main__":
    print(print_items2([12,1,4,8,5]))

# страница 96