"""
selection_sort.py file!
"""

def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированиих значений!
    for i in range(len(nums)):
        # Исходно считаем наименьшим неотсортированным элемент
        lowest_value_index = i
        # Этот цикл перебирает не сортированые элементы!
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке:
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

random_list_of_nums = [12, 8, 3, 10, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)