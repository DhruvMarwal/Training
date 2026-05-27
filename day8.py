# class Edge:
#     def __init__(self, src, dest):
#         self.src = src
#         self.dest = dest

# class DirectedGraph:
#     def createEdges(self, graphList):
#         for i in range(len(graphList)):
#             graphList[i] = []

#         # graphList[0].append(Edge(0,1))
#         # graphList[0].append(Edge(0,2))
#         # graphList[0].append(Edge(0,3))

#         # graphList[1].append(Edge(1,0))
#         # graphList[1].append(Edge(1,2))

#         # graphList[2].append(Edge(2,3))

#     def addEdges(self, graphList, src, dest):
#         graphList[src].append(Edge(src, dest))

#     # def Display(self, graphList):                   
#     #     for a in graphList:
#     #         c = 0
#     #         for i in a:
#     #             if c == 0:
#     #                  print(f"{i.src}: ", end= "")
#     #             print(f"{(i.src, i.dest)}", end= " ")
#     #             c += 1
#     #         print()

#     def Display(self, graphList):
#         for a in graphList:
#             if len(a) == 0:
#                  continue
#             print(f"Paths of {a[0].src}: ", end= "")
#             for i in a:
#                 print(f"{(i.src, i.dest)}", end=" ")
#             print()

# vertices = 4
# graph = DirectedGraph()

# graphList = [None] * vertices

# for i in range(len(graphList)):
#             graphList[i] = []

# graph.createEdges(graphList)

# graph.addEdges(graphList, 0,1)
# graph.addEdges(graphList, 0,2)
# graph.addEdges(graphList, 0,3)
# graph.addEdges(graphList, 1,2)
# graph.addEdges(graphList, 2,3)

# graph.Display(graphList)                    # Paths of 0: (0, 1) (0, 2) (0, 3) 
#                                             # Paths of 1: (1, 2) 
#                                             # Paths of 2: (2, 3) 


#-----------------------------------------------------

# class Edge:
#     def __init__(self, src, dest):
#         self.src = src
#         self.dest = dest

# class UnDirectedGraph:
#     def createEdges(self, graphList):
#         for i in range(len(graphList)):
#             graphList[i] = []

#     def addEdges(self, graphList, src, dest):
#         graphList[src].append(Edge(src, dest))
#         graphList[dest].append(Edge(dest, src))

#     def Display(self, graphList):
#         for a in graphList:
#             if len(a) == 0:
#                  continue
#             print(f"Paths of {a[0].src}: ", end= "")
#             for i in a:
#                 print(f"{(i.src, i.dest)}", end=" ")
#             print()

# vertices = 4
# graph = UnDirectedGraph()

# graphList = [None] * vertices

# for i in range(len(graphList)):
#             graphList[i] = []

# graph.createEdges(graphList)

# graph.addEdges(graphList, 0,1)
# graph.addEdges(graphList, 0,2)
# graph.addEdges(graphList, 0,3)
# graph.addEdges(graphList, 1,2)
# graph.addEdges(graphList, 2,3)

# graph.Display(graphList)                  # Paths of 0: (0, 1) (0, 2) (0, 3) 
                                            # Paths of 1: (1, 0) (1, 2) 
                                            # Paths of 2: (2, 0) (2, 1) (2, 3) 
                                            # Paths of 3: (3, 0) (3, 2) 
