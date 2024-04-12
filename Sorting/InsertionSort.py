def InsertionSort(list):
  for i in range(1, len(list)):
    key = list[i]
    j = i - 1
    while j >= 0 and key < list[j]:
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = key
    print("Pass: ", i, " Key: ", key, " List: ", list)
  return list


InsertionSort([8, 2, 4, 1, 6, 9, 5])
# InsertionSort([8, 2, 4, -1, 6, 9, -5])
# InsertionSort([8, 2, 4, 1, 8, 6, 9, 5])
# InsertionSort([])
