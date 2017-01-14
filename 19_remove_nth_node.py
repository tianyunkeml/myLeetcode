# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		dummy = ListNode(None)
		dummy.next = head
		nodelist = []
		pointer = dummy
		while pointer != None:
			nodelist.append(pointer)
			pointer = pointer.next
		node_before_break = nodelist[-n - 1]
		node_before_break.next = nodelist[-n].next
		return dummy.next
