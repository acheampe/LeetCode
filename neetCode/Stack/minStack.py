import unittest

class MinStack:
    """Each function is in O(1) and O(n) space complexity"""
    def __init__(self):
        self.mainStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        
        self.mainStack.append(val)
        
        if self.minStack and self.minStack[-1] >= val:
            self.minStack.append(val)
        
        elif not self.minStack:
            self.minStack.append(val)

    def pop(self) -> None:
        
        # will always be called on non-empty stack        
        toDelete = self.mainStack.pop()
    
        if toDelete == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        
        # will always be called on non-empty stack
        return self.mainStack[-1] 

    def getMin(self) -> int:
        
         # will always be called on non-empty stack       
        return self.minStack[-1]


class TestMinStack(unittest.TestCase):
    def test_basic_operations(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

    def test_single_element(self):
        stack = MinStack()
        stack.push(5)
        self.assertEqual(stack.top(), 5)
        self.assertEqual(stack.getMin(), 5)
        stack.pop()

    def test_increasing_order(self):
        stack = MinStack()
        for val in [1, 2, 3, 4]:
            stack.push(val)
        self.assertEqual(stack.getMin(), 1)
        stack.pop()
        self.assertEqual(stack.getMin(), 1)

    def test_decreasing_order(self):
        stack = MinStack()
        for val in [4, 3, 2, 1]:
            stack.push(val)
        self.assertEqual(stack.getMin(), 1)
        stack.pop()
        self.assertEqual(stack.getMin(), 2)

if __name__ == '__main__':
    unittest.main()