from Kruskal import Kruskal

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

    kruskalObject = Kruskal()
    kruskalObject.setTerminalOutput(True)
    minSpanningTree = kruskalObject.findMinimalSpanningTree(ex_vertices, ex_edges)
    print(minSpanningTree)
