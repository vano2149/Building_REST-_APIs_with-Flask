"""
sort_by_insert.py file!
"""

def find_Smallest(arr):
  """
  """
  smallest = arr[0] # Для хранения наименьшего значений.
  smallest_index = 0 # Для хранения индекса ниименьшего значения.
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr): # Сортируем список
  newArr = []
  for i in range(len(arr)):
    smallest = find_Smallest(arr) # Находим наименьший элемент в списке
    newArr.append(arr.pop(smallest)) # И добавляем его в новый список!
  return newArr

if __name__ == "__main__":
  print(selectionSort([5, 3, 6, 2 ,10]))