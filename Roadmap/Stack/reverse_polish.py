import math
import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, '/' : operator.truediv}

class Solution:

    def evalRPN(self, lista):

        if len(lista)==1:
            return int(lista[0])

        stack = []
        current_res = 0

        for i in lista:

            if i in ['+', '-', '*', '/']:

                number2 = stack.pop()
                number1 = stack.pop()

                current_res = ops[i](int(number1),int(number2))

                if current_res>0: current_res = math.floor(current_res)
                else: current_res = math.ceil(current_res)

                stack.append(current_res)
            else:
                stack.append(i)

        return current_res

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

a = Solution()

print(a.evalRPN(tokens))
