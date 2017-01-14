class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		pointer1 = l1
		pointer2 = l2
		result = ListNode(None)
		result_pointer = result
		while pointer1 != None or pointer2 != None:
			if (pointer1 != None and pointer2 != None and pointer1.val <= pointer2.val) or (pointer2 == None):
				new_node = ListNode(pointer1.val)
				result_pointer.next = new_node
				pointer1 = pointer1.next
				result_pointer = result_pointer.next
				continue
			if (pointer2 != None and pointer1 != None and pointer2.val < pointer1.val) or (pointer1 == None):
				new_node = ListNode(pointer2.val)
				result_pointer.next = new_node
				pointer2 = pointer2.next
				result_pointer = result_pointer.next
				continue
		return result.next

if __name__ == '__main__':
	l1 = ListNode(2)
	l2 = ListNode(1)
	print Solution().mergeTwoLists(l1, l2).val

