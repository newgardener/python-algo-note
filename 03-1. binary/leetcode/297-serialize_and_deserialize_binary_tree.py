"""
Time Complexity:
- serialize (encode a tree to a single string): O(N)
- deserialize (decode encoded data to a tree): O(N)
ㄴ each node is processed exactly once
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


SEP = ","
NULL = "#"


# %%
# preorder traversal
class Codec:
    def serialize(self, root):
        res = []

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
