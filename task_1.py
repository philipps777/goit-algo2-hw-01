import random


def find_min_max(arr):
  
  if len(arr) <= 1:
    return arr[0], arr[0] 

  mid = len(arr) // 2
  left_min, left_max = find_min_max(arr[:mid])
  right_min, right_max = find_min_max(arr[mid:])

  return min(left_min, right_min), max(left_max, right_max)



def generate_some_array(size):

  return [random.randint(1, 1000) for _ in range(size)]

Some_array = generate_some_array(10)

print(Some_array)

min_value, max_value = find_min_max(Some_array)
print(f"МMin_vailue: {min_value}")
print(f"Max_value: {max_value}")