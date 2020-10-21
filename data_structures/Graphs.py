from collections import defaultdict


# Directed Graph Using adjacency list
# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)
#     def insertEdge(self,v1,v2):
#         self.graph[v1].append(v2)
#     def printGraph(self):
#         for node in self.graph:
#             for v in self.graph[node]:
#                 print(f"{node} => {v}")


# Directed Graph Using adjacency matrix

class Graph:
    def __init__(self, noOfNodes):
        self.noOfNodes = noOfNodes
        self.graph = [[0 for x in range(noOfNodes + 1)] for y in range(noOfNodes + 1)]

    def insertEdge(self, v1, v2):
        if self.withinBound(v1, v2):
            self.graph[v1][v2] = 1

    def withinBound(self, v1, v2):
        return 0 <= v1 <= self.noOfNodes and 0 <= v2 <= self.noOfNodes

    def printGraph(self):
        for i in range(0, self.noOfNodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(f"{i} => {j}")
