from collections import deque


def validateBinaryTreeNodes(
    n: int, leftChild: list[int], rightChild: list[int]
) -> bool:
    indegree = [0] * n
    for i in range(n):
        left = leftChild[i]
        right = rightChild[i]
        if left != -1:
            indegree[left] += 1
        if right != -1:
            indegree[right] += 1

    root = [i for i, d in enumerate(indegree) if d == 0]
    # BST must have one root node
    if not root or len(root) > 1:
        return False

    q = deque(root)
    while q:
        node = q.popleft()
        for child in [leftChild[node], rightChild[node]]:
            if child != -1:
                indegree[child] -= 1
                if indegree[child] > 0:
                    return False
                q.append(child)
    # check if all node's indegree turns 0
    all(d == 0 for d in indegree)
