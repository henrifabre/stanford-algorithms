from dijkstra import dijkstra_path

# inputGrf = {1: [3, 2],
#             2: [3, 4],
#             4: [],
#             3: [4]}
# grfWeight = {(1, 3): 4,
#              (1, 2): 1,
#              (2, 3): 2,
#              (2, 4): 6,
#              (3, 4): 3}
inputGrf = {}
grfWeight = {}
with open("dijkstraData.txt") as f:
        for line in f:
                str = line.split('\t')
                startNode = int(str[0])
                inputGrf[startNode] = []
                for el in str[1:-1]:
                        edge = el.split(',')
                        inputGrf[startNode].append(int(edge[0]))
                        grfWeight[startNode, int(edge[0])] = int(edge[1])

dijkScore = dijkstra_path(inputGrf, grfWeight)
print(dijkScore[7])
print(dijkScore[37])
print(dijkScore[59])
print(dijkScore[82])
print(dijkScore[99])
print(dijkScore[115])
print(dijkScore[133])
print(dijkScore[165])
print(dijkScore[188])
print(dijkScore[197])
