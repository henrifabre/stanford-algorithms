import matplotlib.pyplot as plt
import networkx as nx
import graphs

# inputGrf = {1: ['B', 2],
#                 'E': ['D', 'C'],
#                 'B': ['D', 'C', 1],
#                 'D': ['C', 'B', 'E'],
#                 2: ['C', 1],
#                 'C': [2, 'B', 'D', 'E']}

inputGrf = {}
inputGrfR = {}
with open("SCC.txt") as f:
        for line in f:
                edge = line.split()
                startNode = int(edge[0])
                endNode = int(edge[1])
                if startNode in inputGrf:
                        inputGrf[startNode].append(endNode)
                else:
                        inputGrf[startNode] = [endNode]
                if endNode not in inputGrf:
                        inputGrf[endNode] = []

                if endNode in inputGrfR:
                        inputGrfR[endNode].append(startNode)
                else:
                        inputGrfR[endNode] = [startNode]
                if startNode not in inputGrfR:
                        inputGrfR[startNode] = []


# print(inputGrf)
nxDrawGraph = False

if len(inputGrf) > 50:
        nxDrawGraph = False

seen_order, explored_order = graphs.graph_findSCC(inputGrf, inputGrfR)
# print("Seen Order:  ")
# print(seen_order)
# print("Explored Order:  ")
# print(explored_order)
scc_size = []
for el in explored_order:
        scc_size.append(len(el))
scc_size.sort(reverse=True)
print(scc_size[:5])
print(len(scc_size))

if nxDrawGraph is True:
        nxGrf = nx.DiGraph(inputGrfR)
        nx.draw(nxGrf, pos=nx.shell_layout(inputGrf), with_labels=True)
        plt.show()
