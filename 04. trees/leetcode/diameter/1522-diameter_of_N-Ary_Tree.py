from typing import Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[list["Node"]] = None
    ):
        self.val = val
        self.children = children if children is not None else []


def diameter(root: "Node") -> int:
    longest = 0

    def dfs(node):
        nonlocal longest
        if not node:
            return 0
        d = []
        for child in node.children:
            d.append(dfs(child))
        d.sort()
        path = d[-1] + d[-2] if len(d) >= 2 else d[-1]
        # update the longest diameter up to this point
        longest = max(longest, path)
        # should return the longest path among children
        return d[-1] + 1

    dfs(root)
    return longest
