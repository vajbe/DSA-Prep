import math


def BucketSort(list):
  numBuckets = round(math.sqrt(len(list)))
  maxValue = max(list)

  arr = []
  for i in range(numBuckets):
    arr.append([])

  for i in list:
    bucketIndex = math.ceil((i * numBuckets) / maxValue)
    arr[bucketIndex - 1].append(i)

  for i in range(numBuckets):
    arr[i].sort()

  k = 0
  for i in range(numBuckets):
    for j in range(len(arr[i])):
      list[k] = arr[i][j]
      k += 1
  print(list)


BucketSort([8, 2, 4, 1, 6, 9, 5])
BucketSort([8, 2, 4, 1, 8, 6, 9, 5])
BucketSort([50, 14, 55, 24, 90, 46])
