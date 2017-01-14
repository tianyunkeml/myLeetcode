class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minVal == None or x < self.minVal:
            self.minVal = x


    def pop(self):
        """
        :rtype: void
        """
        if self.minVal == self.stack[-1]:
            self.minVal = min(self.stack[:-1]) if len(self.stack) > 1 else None
        del self.stack[-1]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal