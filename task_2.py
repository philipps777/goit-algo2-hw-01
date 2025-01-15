import random

def generate_some_array(size):

  return [random.randint(1, 1000) for _ in range(size)]

def quick_select(arr, k):
 

  def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
      if array[j] <= pivot:
        i = i + 1
        array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

  def quick_select_helper(arr, low, high, k):
    if low == high:
      return arr[low]
    
    pi = partition(arr, low, high)

    if pi - low == k - 1:
      return arr[pi]
    elif pi - low > k - 1:
      return quick_select_helper(arr, low, pi - 1, k)
    else:
      return quick_select_helper(arr, pi + 1, high, k - pi + low - 1)

  return quick_select_helper(arr, 0, len(arr) - 1, k - 1)


array_size = 10  
Some_array = generate_some_array(array_size)


k = random.randint(1, array_size-3) 

print("Generated array:", Some_array)
print("Value k:", k)

kth_smallest = quick_select(Some_array, k)
print(f"{k}  - minimum element: {kth_smallest}") 