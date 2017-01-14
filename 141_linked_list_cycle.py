class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
        """
        length1, length2 = 1
        if head == None:
        	return False
        nextNode = head.next
        while nextNode != None:
        	length1 += 1
        	temp = nextNode.next
        	nextNode.next = None
        	nextNode = temp
        

        