x = 2
y = 3
# print(x ^ y)

arr = [6,2,7,3]
res = [1]
first = 4
for i in arr:  
  print(first^i)
  first = first ^ i
  res.append(first)
