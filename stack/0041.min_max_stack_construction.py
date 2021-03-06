# Min Max Stack Construction
# ----------------------------

# Problem Statement
# ------------------

# Write a Min Max Stack class. The class should support pushing and popping values on and off the stack,
# peeking at values at the top of the stack, and getting both the minimum and the maximum values in the stack. 
# All class methods, when considered independently, should run in constant time and with constant space
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

# 
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
    
    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) -1]

    # O(1) time | O(1) space    
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # O(1) time | O(1) space
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)

        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
    
    # O(1) time | O(1) space    
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["min"]
    
    # O(1) time | O(1) space    
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["max"]

stack = MinMaxStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("peek: ", stack.peek())
print("pop: ", stack.pop())
print("min: ", stack.getMin())
print("max: ", stack.getMax())
