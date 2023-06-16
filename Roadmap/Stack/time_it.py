import timeit


testcode = '''

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()

'''

print(timeit.timeit(stmt=testcode, setup="from min_stack import MinStack",number=100))


