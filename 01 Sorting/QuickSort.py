def partition(list, low, high):
  #Track the high element
  i = low - 1
  pivot = list[high]

  for j in range(low, high):
    if list[j] <= pivot:
      i = i + 1
      (list[i], list[j]) = (list[j], list[i])
  #Swap the pivot and high element
  (list[i + 1], list[high]) = (list[high], list[i + 1])
  return i + 1


def quick(list, low, high):
  if (low < high):
    pi = partition(list, low, high)
    quick(list, pi + 1, high)
    quick(list, low, pi - 1)


cList = [8, 2, 4, 1, 6, 9, 5]
quick(cList, 0, len(cList) - 1)
print(cList)
