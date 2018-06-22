# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                val.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                val.append('#')
        val=[]
        helper(root)
        return ' '.join(val)
        
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val=next(vals)
            if val=='#':
                return None
            root=TreeNode(int(val))
            root.left=helper()
            root.right=helper()
            return root
        vals=iter(data.split())
        return helper()
        
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))