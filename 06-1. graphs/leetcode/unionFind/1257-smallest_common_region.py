class Solution:
    def getPathForRegion(self, node, childParentMap):
        path = [node]
        while node in childParentMap:
            parent = childParentMap[node]
            path.append(parent)
            node = parent
        return path

    def findSmallestRegion(
        self, regions: list[list[str]], region1: str, region2: str
    ) -> str:
        childParentMap = {}
        for region in regions:
            parent = region[0]
            for child in regions[1:]:
                childParentMap[child] = parent

        path1 = self.getPathForRegion(region1, childParentMap)
        path2 = self.getPathForRegion(region2, childParentMap)

        i, j = 0, 0
        while i < len(path1) and j < len(path2) and path1[i] != path2[j]:
            i += 1
            j += 1
        return path1[i]



