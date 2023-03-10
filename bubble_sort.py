"""
bubble_sort.py file!
"""

def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотябы 1-н раз.
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элументы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
