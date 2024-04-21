# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:

  def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for token in tokens:
      if token == '+' or token == '/' or token == '*' or token == '-':
        # print(stack)
        b = int(stack.pop())
        a = int(stack.pop())
        match token:
          case "+":
            stack.append(str(a + b))
          case "-":
            stack.append(str(a - b))
          case "/":
            stack.append(int((a / b)))
          case "*":
            stack.append(str(a * b))
      else:
        stack.append(token)
    return int(stack[0])
