class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		global max_depth
		max_depth = 0

		if root == None:
			return 0
		def traverse(t, depth):
			global max_depth
			if t.left != None:
				traverse(t.left, depth + 1)
			if depth > max_depth:
				max_depth = depth
			if t.right != None:
				traverse(t.right, depth + 1)
		traverse(root, 1)
		return max_depth

