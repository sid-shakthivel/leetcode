class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(token))

        return stack[0]

