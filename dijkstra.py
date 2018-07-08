def dijkstra_path(inputGrf, grfWeight, startNode=1):
        procVert = set()
        procVert.add(startNode)
        # inprocVert = set()
        # inprocVert.add(2)
        # inprocVert.add(3)
        inprocScore = {}
        unprocVert = set()
        for node in inputGrf:
                unprocVert.add(node)
        for edge in inputGrf[startNode]:
                inprocScore[edge] = grfWeight[startNode, edge]
                unprocVert.remove(edge)
        unprocVert.remove(startNode)

        dijkScore = {startNode: 0}
        while len(inprocScore) > 0:
                # Choose smallest edge
                minNode = min(inprocScore, key=inprocScore.get)
                minScore = inprocScore[minNode]
                # minScore = 999999999
                # minNode = None
                # for node in inprocScore:
                #         if minScore > inprocScore[node]:
                #                 minScore = inprocScore[node]
                #                 minNode = node
                # Move from in process to processed, add score
                dijkScore[minNode] = minScore
                procVert.add(minNode)
                del inprocScore[minNode]
                # Calculate score for vertices emanating from this node
                for edge in inputGrf[minNode]:
                        if edge in inprocScore:
                                if inprocScore[edge] > (dijkScore[minNode] + grfWeight[minNode, edge]):
                                        inprocScore[edge] = dijkScore[minNode] + grfWeight[minNode, edge]
                        elif edge in unprocVert:
                                # print(minNode)
                                inprocScore[edge] = dijkScore[minNode] + grfWeight[minNode, edge]
                                unprocVert.remove(edge)
                        elif edge in procVert:
                                continue
                        else:
                                print("Error!!")
        return dijkScore
