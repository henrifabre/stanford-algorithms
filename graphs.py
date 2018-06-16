from collections import deque


def graphsearch_bfs(graph, startNode, bfs_explored_nodeList=[]):
        node_queue = deque()    # Invariant - does not contain explored nodes
        node_queue.append(startNode)
        bfs_explored_nodeList.append(startNode)
        while node_queue:
                current_node = node_queue.popleft()
                for node in graph[current_node]:
                        if node not in bfs_explored_nodeList:
                                node_queue.append(node)
                                bfs_explored_nodeList.append(node)

        return bfs_explored_nodeList


def graphsearch_dfs(graph, startNode, dfs_seen_nodeList=[]):
        node_stack = deque()
        node_stack.append(startNode)
        dfs_seen_nodeList.append(startNode)
        for node in graph[startNode]:
                if node not in dfs_seen_nodeList:
                        graphsearch_dfs(graph, node, dfs_seen_nodeList)

        return dfs_seen_nodeList


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
