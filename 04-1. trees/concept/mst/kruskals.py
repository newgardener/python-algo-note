class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1


def kruskals_mst(vertices, edges):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(vertices)
    mst = []
    mst_cost = 0
    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, cost))
            mst_cost += cost
            if len(mst) == len(edges) - 1:
                break
    return mst, mst_cost


vertices = 5
edges = [(0, 1, 10), (0, 3, 5), (1, 2, 1), (1, 3, 2), (2, 3, 9), (2, 4, 4), (3, 4, 7)]

mst, mst_cost = kruskals_mst(vertices, edges)
print(mst, mst_cost)
