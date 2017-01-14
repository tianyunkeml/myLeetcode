class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        length = len(self.stack)
        self.stack = [x] + self.stack
        for i in range(length):
            self.stack = [self.stack[-1]] + self.stack
            del self.stack[-1]

    def pop(self):
        """
        :rtype: nothing
        """
        del self.stack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0