# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		list1 = []
		list2 = []
		order1 = []
		order2 = []
		cursor1 = p
		cursor2 = q
		def traverse(t, list, order):
			if t.left != None:
				order.append(1)
				traverse(t.left, list, order)
			list.append(t.val)
			if t.right != None:
				order.append(2)
				traverse(t.right, list, order)
		if p != None:
			traverse(p, list1, order1)
		if q != None:
			traverse(q, list2, order2)
			
		if list1 == list2 and order1 == order2:
			return True
		else:
			return False
