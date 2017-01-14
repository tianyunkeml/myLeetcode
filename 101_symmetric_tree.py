class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		list1 = []
		list2 = []
		order1 = []
		order2 = []
		if root == None:
			return True
		def traverse(t, list, order):
			if t.left != None:
				order.append(1)
				traverse(t.left, list, order)
			list.append(t.val)
			if t.right != None:
				order.append(2)
				traverse(t.right, list, order)
		def traverse2(t, list, order):
			if t.right != None:
				order.append(1)
				traverse2(t.right, list, order)
			list.append(t.val)
			if t.left != None:
				order.append(2)
				traverse2(t.left, list, order)
		traverse(root, list1, order1)
		traverse2(root, list2, order2)
		print list1
		print list2
		print order1
		print order2
		if list1 == list2 and order1 == order2:
			return True
		else:
			return False
