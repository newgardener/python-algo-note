from collections import deque


def validateBinaryTreeNodes(
    n: int, leftChild: list[int], rightChild: list[int]
) -> bool:
    children = set(leftChild + rightChild)
    children.discard(-1)
    # no root case
    if len(children) == n:
        return False

    root = next(i for i in range(n) if i not in children)
    visited = [False] * n
    visited[root] = True
    q = deque([root])
    while q:
        node = q.popleft()
        for child in [leftChild[node], rightChild[node]]:
            if child == -1:
                continue
            # cycle detection
            if visited[child]:
                return False
            visited[child] = True
            q.append(child)
    # at the end, if all nodes are visited then it is valid binary tree nodes
    return all(visited)
