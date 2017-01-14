class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		global min_depth
		min_depth = -1

		if root == None:
			return 0
		def traverse(t, depth):
			global min_depth
			if t.left != None:
				traverse(t.left, depth + 1)
			if t.right != None:
				traverse(t.right, depth + 1)
			if t.left == None and t.right == None and (depth < min_depth or min_depth == -1):
				print t.val
				print depth
				min_depth = depth
		traverse(root, 1)
		return min_depth