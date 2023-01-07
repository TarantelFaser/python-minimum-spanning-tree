# first element just for filling, so indexing = vertex numbers
P = []


def kruskal(vertices, edges):
    # initializing
    global P
    minSpanningTree = []
    P.append(None)
    for v in vertices:
        P.append(v)

    edgesSorted = sortEdges(edges)

    partCount = len(vertices)
    while partCount > 1:
        print(P)
        smallestEdge = edgesSorted.pop(0)
        set1 = find(smallestEdge[0][0])
        set2 = find(smallestEdge[0][1])
        if set1 != set2:
            union(set1, set2)
            partCount -= 1
            minSpanningTree.append(smallestEdge)

    return minSpanningTree


# using bubblesort here ... not very efficient
def sortEdges(edgeArray):
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
def union(rootPart1, rootPart2):
    global P
    part1Length = 0
    part2Length = 0
    for i in range(1, 9):
        if P[i] == rootPart1:
            part1Length += 1
        elif P[i] == rootPart2:
            part2Length += 1

    if part1Length < part2Length:
        P[rootPart1] = rootPart2
    else:
        P[rootPart2] = rootPart1


# find root of tree in which vertex is
def find(vertex):
    global P
    S = []
    S.insert(0, vertex)
    while P[vertex] != vertex:
        vertex = P[vertex]
        S.insert(0, vertex)
    for w in S:
        P[w] = vertex
    return vertex


# example
if __name__ == '__main__':
    ex_vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ex_edges = [
        [[1, 2], 1],
        [[1, 3], 3],
        [[1, 7], 7],
        [[2, 5], 9],
        [[3, 4], 2],
        [[3, 5], 10],
        [[4, 5], 11],
        [[5, 6], 4],
        [[5, 9], 16],
        [[5, 7], 6],
        [[5, 8], 15],
        [[7, 8], 5]
    ]

    minSpanningTree = kruskal(ex_vertices, ex_edges)
    print(minSpanningTree)
