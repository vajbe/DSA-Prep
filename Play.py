str = "((a+b))"
stack = []
for ch in str:
  if ch == ')':
    print(stack)
    top = stack.pop()
    flag = True
    while (top != '('):
      if (top == '+' or top == '-' or top == '*' or top == '/'):
        flag = False
        print("Yes wrong")
      top = stack.pop()
      # stack.pop()
    if flag == True:
      print("Yes")
  else:
    stack.append(ch)
print("No")

# print(stack)
