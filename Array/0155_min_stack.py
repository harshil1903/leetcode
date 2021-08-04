
# 155. Min Stack
#
# Source : https://leetcode.com/problems/min-stack/
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    # push a pair of value and minimum element to the stack list
    def push(self, val: int) -> None:
        if self.stack:
            current_min = min(val, self.stack[-1][0])
            self.stack.append((current_min, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        return self.stack.pop()[1]

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2