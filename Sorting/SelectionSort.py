def SelectionSort(list):
  for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
      if list[min_index] > list[j]:
        min_index = j
    list[min_index], list[i] = list[i], list[min_index]
  print(list)


SelectionSort([8, 2, 4, 1, 6, 9, 5])
SelectionSort([8, 2, 4, -1, 6, 9, -5])
SelectionSort([8, 2, 4, 1,8, 6, 9, 5])
SelectionSort([])

