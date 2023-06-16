class MinStack:

    def __init__(self):

    	self.stack = []
    	self.min = []

    def push(self, number):

    	self.stack.append(number)

    	if self.min == []:
    		self.min.append(number)

    	elif number<=self.getMin():
    		self.min.append(number)

    	return None
        

    def pop(self):

    	pop = self.stack.pop()

    	if self.getMin() == pop: self.min.pop()


    	return None
        

    def top(self):

    	return self.stack[len(self.stack)-1]
        

    def getMin(self):
    	return self.min[len(self.min)-1]

# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(2147483646)
print(obj.min)
obj.push(2147483646)
obj.push(2147483647)
obj.top()
obj.pop()

obj.getMin()
obj.pop()
obj.getMin()
obj.pop()
obj.push(2147483647)
obj.top()
obj.getMin() #
# obj.push(-2147483648)
# obj.top()
# obj.getMin()
# obj.pop()
# obj.getMin()#



