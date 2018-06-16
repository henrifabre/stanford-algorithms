import matplotlib.pyplot as plt
import networkx as nx
import graphs

inputGrf = {'S': ['B', 'A'],
                'E': ['D', 'C'],
                'B': ['D', 'C', 'S'],
                'D': ['C', 'B', 'E'],
                'A': ['C', 'S'],
                'C': ['A', 'B', 'D', 'E']}

nxDrawGraph = True
if nxDrawGraph is True:
        nxGrf = nx.Graph(inputGrf)
        nx.draw(nxGrf, with_labels=True)
        plt.show()

bfs_order = graphs.graphsearch_dfs(inputGrf, 'S')
print("BFS Order:  ")
print(bfs_order)
