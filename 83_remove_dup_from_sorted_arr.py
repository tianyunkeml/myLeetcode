# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		cursor = head
		if head == None:
			return None
		while cursor.next != None:
			if cursor.val == cursor.next.val:
				cursor.next = cursor.next.next
			else:
				cursor = cursor.next
		return head