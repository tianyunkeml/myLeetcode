class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		def getLength(head):
			result = 0
			cursor = head
			while cursor != None:
				result += 1
				cursor = cursor.next
			return result

		result = None
		lenA = getLength(headA)
		lenB = getLength(headB)
		if getLength(headA) * getLength(headB) == 0:
			return None
		if lenA > lenB:
			for n in range(lenA - lenB):
				headA = headA.next
		elif lenB > lenA:
			for n in range(lenB - lenA):
				headB = headB.next
		cursorA = headA
		cursorB = headB
		while cursorA != None:
			if cursorA == cursorB:
				return cursorA
				break
			cursorA = cursorA.next
			cursorB = cursorB.next
		return result

        