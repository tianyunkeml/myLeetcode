class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		dummy = ListNode(None)
		dummy.next = head
		cursor = dummy
		while cursor.next != None:
			if cursor.next.val == val:
				cursor.next = cursor.next.next
			else:
				cursor = cursor.next
		return dummy.next
