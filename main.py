# def extendList(nums):
#   nums.extend(nums)
#   return nums

# a = [1,2,1]
# a = extendList(a)
# print(a)

# def numIdenticalPairs(nums):
#   pairs = 0
#   for i in range(len(nums)):
#       for j in range(i+1, len(nums)):
#         if(nums[i] == nums[j]):
#           print(i,j)
#           pairs += 1
#   return pairs

# print(numIdenticalPairs([1,2,3,1,1,3]))

# def findWordsContaining(words, x):
#   res = []
#   for indx, word in enumerate(words):
#     if x in word:
#       res.append(indx)
#   return res

# print(findWordsContaining(["leet", "code"], "z"))
# print(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
def maxWidthOfVerticalArea(points):
  p = sorted(points, key=lambda x: x[0])
  max_width = 0
  print(p)
  for i in range(1, len(p)):
    max_width = max(max_width, p[i][0] - p[i-1][0])
  return max_width
print(maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))