# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize1(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        serial = ""
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                serial += "null,"
            else:
                serial += str(node.val) + ','
                stack.append(node.right)
                stack.append(node.left)
           
            
        print(serial[:-1])
        return serial[:-1]
            
    def serialize(self, root):
        def r_serialize(node, s):
            if not node:
                return s + "null,"
            else:
                s = r_serialize(node.left, s + str(node.val) + ",")
                s = r_serialize(node.right, s)
                return s

        return r_serialize(root, "")
        
    def deserialize(self, data):
        serial = data[:-1].split(",")
        
        def r_deserialize(s):
            if s[0] == "null":
                s.pop(0)
                return None
            node = TreeNode(int(s[0]))
            s.pop(0)
            node.left = r_deserialize(s)
            node.right = r_deserialize(s)
            return node
        
        return r_deserialize(serial)
            
            
            
            
    def deserialize1(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        serial = data.split(",")
        stack = []
        for val in serial:
            if not stack:
                root = TreeNode(int(val))
                stack.append([root, True])
            else:
                node, state = stack[-1]
                if not node.left and state:
                    if val == "null":
                        stack[-1][1] = False
                    else:
                        left_node = TreeNode(int(val))
                        node.left = left_node
                        print(left_node.val)
                        stack.append([left_node, True])
                else:
                    stack.pop()
                    if not val == "null":
                        right_node = TreeNode(int(val))
                        node.right = right_node
                        print(right_node.val)
                        stack.append([right_node, True])
        return root
        
                        
                    
                
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
