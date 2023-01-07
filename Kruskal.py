
class Kruskal:
    __P = None

    def __init__(self):
        self.__P = []

    def findMinimalSpanningTree(self, vertices, edges):
        # initializing
        minSpanningTree = []
        self.__P.append(None)
        for v in vertices:
            self.__P.append(v)

        edgesSorted = self.__sortEdges(edges)

        partCount = len(vertices)
        while partCount > 1:
            print(self.__P)
            smallestEdge = edgesSorted.pop(0)
            set1 = self.__find(smallestEdge[0][0])
            set2 = self.__find(smallestEdge[0][1])
            if set1 != set2:
                self.__union(set1, set2)
                partCount -= 1
                minSpanningTree.append(smallestEdge)

        return minSpanningTree

    # using bubblesort ... not optimal
    def __sortEdges(self, edgeArray):
        hasChanged = True
        while hasChanged:
            hasChanged = False
            for i in range(0, len(edgeArray) - 1):
                if edgeArray[i][1] > edgeArray[i + 1][1]:
                    h = edgeArray[i]
                    edgeArray[i] = edgeArray[i + 1]
                    edgeArray[i + 1] = h
                    hasChanged = True
        return edgeArray

    # combine to trees to one
    def __union(self, rootPart1, rootPart2):
        part1Length = 0
        part2Length = 0
        for i in range(1, 9):
            if self.__P[i] == rootPart1:
                part1Length += 1
            elif self.__P[i] == rootPart2:
                part2Length += 1

        if part1Length < part2Length:
            self.__P[rootPart1] = rootPart2
        else:
            self.__P[rootPart2] = rootPart1

    # find root of tree in which vertex is
    def __find(self, vertex):
        S = []
        S.insert(0, vertex)
        while self.__P[vertex] != vertex:
            vertex = self.__P[vertex]
            S.insert(0, vertex)
        for w in S:
            self.__P[w] = vertex
        return vertex
