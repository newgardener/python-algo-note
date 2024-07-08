"""
Time Complexity:
- serialize: O(N)
- deserialize: O(N)
ㄴ each node is processed exactly once
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


SEP = ","
NULL = "#"


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        # preorder traversal
        def dfs(node):
            if not node:
                res.append(NULL)
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return SEP.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

          :type data: str
          :rtype: TreeNode
          """
        nodes = data.split(SEP)[::-1]

        def dfs():
            val = nodes.pop()
            if val == NULL:
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
