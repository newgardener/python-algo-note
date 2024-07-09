"""
Time Complexity:
- serialize (encode a tree to a single string): O(N)
- deserialize (decode encoded data to a tree): O(N)
ㄴ each node is processed exactly once
"""
import collections


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


# %%
# postorder traversal
class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append(NULL)
                return
            dfs(node.left)
            dfs(node.right)
            res.append(str(node.val))

        dfs(root)
        return SEP.join(res)

    def deserialize(self, data):
        nodes = data.split(SEP)

        def dfs():
            val = nodes.pop()
            if val == NULL:
                return None
            node = TreeNode(val)
            # create right subtree first before left subtree
            node.right = dfs()
            node.left = dfs()
            return node

        return dfs()


# %%
# level-order traversal
class Codec:
    def serialize(self, root):
        def levelOrder(start):
            res = []
            q = collections.deque([start])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if not node:
                        res.append(NULL)
                        continue
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
            return SEP.join(res)

        return levelOrder(root)

    def deserialize(self, data):
        nodes = data.split(SEP)

        rootVal = nodes[0]
        if rootVal == NULL:
            return None

        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        i = 1
        while i < len(nodes):
            parent = q.popleft()
            # left child
            left = nodes[i]
            i += 1
            if left == NULL:
                parent.left = None
            else:
                parent.left = TreeNode(int(left))
                q.append(parent.left)
            # right child
            right = nodes[i]
            i += 1
            if right == NULL:
                parent.right = None
            else:
                parent.right = TreeNode(int(right))
                q.append(parent.right)
        return root
