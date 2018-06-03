def ...(self,nums):
	def BST_helper(nums,left,right):
		if left>right:
			return None
		if left==right:
			return TreeNode(nums[left])
		else:
			middle=(left+right)/2
			node=TreeNode(nums[middle])
			node.left=self.BST_helper(nums,left,middle-1)
			node.right=self.BST_helper(nums,middle+1,right)
			return node
	return BST_helper(nums,0,len(nums)-1)