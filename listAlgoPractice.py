def swap(input_list, index_1, index_2):
  temp = input_list[index_1]
  input_list[index_1] = input_list[index_2]
  input_list[index_2] = temp
  return input_list

def selection_sort(my_list):
  for j in range(len(my_list)):
    lowest_index = j
    for i in range(j, len(my_list)):
      if my_list[i] < my_list[lowest_index]:
        lowest_index = i
    my_list = swap(my_list, lowest_index, j)
  return my_list

# Test the function on two different lists
list1 = [8, 15, 4, 2]
list2 = [10, -3, 0, 5, 1]

sorted1 = selection_sort(list1)
sorted2 = selection_sort(list2)

print(sorted1)  # Output: [2, 4, 8, 15]
print(sorted2)  # Output: [-3, 0, 1, 5, 10]
