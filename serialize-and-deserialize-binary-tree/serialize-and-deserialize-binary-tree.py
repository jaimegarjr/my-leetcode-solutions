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
        
        res = []
        
        q = collections.deque([root])
        
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
            
                if not node:
                    res.append("null")
                    continue
                
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        
        if nodes[0] == "null":
            return None
        
        root = TreeNode(int(nodes[0]))
        nodes.pop(0)
        q = collections.deque([root])
        
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                if nodes[0] != "null":
                    node.left = TreeNode(int(nodes[0]))
                    q.append(node.left)
                nodes.pop(0)
                
                if nodes[0] != "null":
                    node.right = TreeNode(int(nodes[0]))
                    q.append(node.right)
                nodes.pop(0)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))