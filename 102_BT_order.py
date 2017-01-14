class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		global result
		result = []
		if node == None:
			return result
		def traverse(node, depth):
			global result
			if node.left != None:
				traverse(node.left, depth + 1)

			value = node.val
			while depth + 1 > len(result):
				result.append([])
			result[depth].append(value)
			if node.right != None:
				traverse(node.right, depth + 1)
		traverse(root, 0)
		return result

        