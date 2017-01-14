class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        buffer = []
        length = len(self.queue)
        for i in range(length):
            buffer = [self.queue[-1]] + buffer
            del self.queue[-1]
        self.queue.append(x)
        for n in buffer:
            self.queue.append(n)



    def pop(self):
        """
        :rtype: nothing
        """
        del self.queue[-1]


    def peek(self):
        """
        :rtype: int
        """
        return self.queue[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0