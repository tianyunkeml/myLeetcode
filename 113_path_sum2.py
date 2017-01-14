# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Important! Watchout the ref of list. Dynamic or copy!

class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		global result
		global givenSum
		result = []
		givenSum = sum

		if root == None:
			return []
		def pathSum(t, accSum, currentList):
			global givenSum
			global result
			if t.left == None and t.right == None and accSum == sum:
				result.append(currentList[:])      # This is a copy!!!!
			if t.left != None:
				newList = currentList
				newList.append(t.left.val)
				pathSum(t.left, accSum + t.left.val, newList)
				currentList.pop()
			if t.right != None:
				newList = currentList
				newList.append(t.right.val)
				pathSum(t.right, accSum + t.right.val, newList)
				currentList.pop()
		pathSum(root, root.val, [root.val])
		return result