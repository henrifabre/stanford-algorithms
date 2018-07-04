from collections import deque
import copy
# import line_profiler


def graphsearch_bfs(graph, startNode, explored_nodeList=[]):
        node_queue = deque()    # Invariant - does not contain explored nodes
        node_queue.append(startNode)
        explored_nodeList.append(startNode)
        while node_queue:
                current_node = node_queue.popleft()
                for node in graph[current_node]:
                        if node not in explored_nodeList:
                                node_queue.append(node)
                                explored_nodeList.append(node)

        return explored_nodeList


# @profile
def graphsearch_dfs(graph, startNode, seen_nodeList=set(), explored_nodeStack=[]):
        nodeStack = []
        if startNode not in seen_nodeList:
                seen_nodeList.add(startNode)
                nodeStack.append(startNode)
        while nodeStack:
                currentNode = nodeStack[-1]
                exploredFlag = True
                for node in graph[currentNode]:
                        if node not in seen_nodeList:
                                nodeStack.append(node)
                                seen_nodeList.add(node)
                                exploredFlag = False
                if exploredFlag:
                        explored_nodeStack.append(nodeStack.pop())

        return seen_nodeList, explored_nodeStack


# DFS search using recursive method
# def graphsearch_dfs(graph, startNode, seen_nodeList=deque(), explored_nodeStack=deque()):
#         if startNode not in seen_nodeList:
#                 seen_nodeList.append(startNode)
#         for node in graph[startNode]:
#                 if node not in seen_nodeList:
#                         graphsearch_dfs(graph, node, seen_nodeList, explored_nodeStack)
#         explored_nodeStack.append(startNode)
#         return seen_nodeList, explored_nodeStack


# Assumption: graph is a dict with keys as ardered integers starting from 1
#             because we start exploring the graph from vertex 1
# @profile
def graph_findSCC(graph, graphR, seen_nodeList=set(), explored_nodeStack=[]):
        # 1st pass
        for i in range(1, max(graph)+1):
                if i not in seen_nodeList:
                        seen_nodeList, explored_nodeStack = graphsearch_dfs(
                                graph, i, seen_nodeList=seen_nodeList)

        # 2nd pass

        seen_nodeList.clear()
        scc_list = []
        unexplored_nodeStack = copy.deepcopy(explored_nodeStack)
        unexplored_nodeSet = set(unexplored_nodeStack)
        print("First pass done")
        while unexplored_nodeStack:
                scc_list.append([unexplored_nodeStack.pop()])
                unexplored_nodeSet.remove(scc_list[-1][0])
                seen_nodeList, __t = graphsearch_dfs(graphR,
                                                     startNode=scc_list[-1][0],
                                                     seen_nodeList=seen_nodeList)
                newlySeenNodeSet = seen_nodeList & unexplored_nodeSet
                for el in newlySeenNodeSet:
                        scc_list[-1].append(el)
                        # unexplored_nodeStack.remove(el)
                        unexplored_nodeSet.remove(el)
                while unexplored_nodeStack and unexplored_nodeStack[-1] in seen_nodeList:
                        unexplored_nodeStack.pop()

        return seen_nodeList, scc_list


def find_path(graph, start, end, path=[]):
        if start not in graph:
                return None
        paths = []
        path = path + [start]
        if start == end:
                return [path]

        for node in graph[start]:
                if node not in path:
                        newpath = find_path(graph, node, end, path)
                        for newpaths in newpath:
                                paths.append(newpaths)

        return paths


# paths = find_path(graph, 'A', 'D')
# print(paths)
