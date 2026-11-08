class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        # iterate through numbers and add to stack until non-number found
        # then apply non-number to last 2 values in stack, add result to stack
        
        stack = []

        for token in tokens:
            try:
                token = int(token)
                stack.append(token)

            except: #handle operator
                result = 0
                if token == "+":
                    result = stack[-2] + stack[-1]
                elif token == "-":
                    result = stack[-2] - stack[-1]
                elif token == "*":
                    result = stack[-2] * stack[-1]
                else:
                    result = int(stack[-2] / stack[-1])
                print(result)
                stack.pop()
                stack.pop()
                stack.append(result)
        
        return stack[0]
                