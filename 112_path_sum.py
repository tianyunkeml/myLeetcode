class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def hasPathSum(self, root, givenSum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		global sum
		global result

		sum = givenSum
		if root == None:
			return False
		result = False
		def pathSum(t, accSum):
			global sum
			global result
			if t.left == None and t.right == None and accSum == sum:
				result = True
				return -1
			if t.left != None:
				if pathSum(t.left, accSum + t.left.val) == -1:
					return -1
			if t.right != None:
				if pathSum(t.right, accSum + t.right.val) == -1:
					return -1
		pathSum(root, root.val)
		return result
