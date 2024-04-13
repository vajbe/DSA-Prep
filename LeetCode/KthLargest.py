#ToDo Not Working


def findKthLargest(nums, k):
  numsList = [0] * len(nums)
  el = len(numsList) - (k)
  for i in range(0, len(nums)):
    num = nums[i]
    numsList[num - 1] = num
  print(numsList[el])
  print(numsList)


findKthLargest([3, 2, 1, 5, 6, 4], 2)
findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
