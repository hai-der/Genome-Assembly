# Haider Tiwana
# CS465: Bioinformatics
# Problem Set #3

# build Graph
def buildGraph(kmers, vertices):
    graph = {}
    for i in range(len(vertices)):
        graph[i] = []
        for j in range(len(vertices)):
            for item in kmers:
                if vertices[i] == item[:-1] and vertices[j] == item[1:]:
                    graph[i].append(j)
    return graph

# build Matrix
def buildMatrix(graph, vertices):
    matrix = [[0]*len(vertices) for _ in range(len(vertices))]
            
    for m in graph:
        for n in graph:
            if n in graph[m]:
                matrix[m][n] = 1

    return matrix

# build Edges
def buildEdges(graph, vertices):
    edges = []
    for m in graph:
        for n in graph:
            if n in graph[m]:
                edges.append((m,n))

    return edges

# build a list of column totals
def sum1(input):
    return map(sum, input)

def main():
    filename = input("Enter filename: ")
    file = open(filename, 'r')
    kmers = []
    for line in file:
        line = line.strip()
        kmers.append(line)

    # append vertices to list
    myVertices = []
    for item in kmers:
        if item[:-1] not in myVertices:
            myVertices.append(item[:-1])
        if item[1:] not in myVertices:
            myVertices.append(item[1:])

    print(myVertices)
    myGraph = buildGraph(kmers, myVertices)
    print(myGraph)
    myMatrix = buildMatrix(myGraph, myVertices)
    print("\n", myMatrix)


    start = -1
    end = -1

    row_totals = []
    col_totals = []
    
    # sum the rows
    for row in range(len(myMatrix)):
        row_totals.append(sum(myMatrix[row]))
        if sum(myMatrix[row]) == 0:
            end = row
    # sum the columns
    col_totals = [sum(x) for x in zip(*myMatrix)]

   # print("Row totals are", row_totals)
   # print("Column sums are", col_totals)

    # if start isn't found, use 0
    for x in range(len(col_totals)):
        if col_totals[x] == sum(myMatrix[x])-1:
            start = x
            break
        else:
            start = 0

    print("Start is", start)
    print("End is", end)

    myEdges = buildEdges(myGraph, myVertices)

    print("Your edges are", myEdges, "\n")
    
    # grow path until all edges have been used
    current = start
    path = [current]
    myStarts = []
    nextItem = 1

   # if isEularian(row_totals, col_totals):
    while len(myEdges) > 0:
        for item in myEdges:
            myStarts.append(item[0])
            
        if current in myStarts:
            for item in myEdges:
                if item[0] == current:
                    path.insert( nextItem, item[1])
                    nextItem += 1
                    current = item[1]
                   # print("Current is", current)
                    myEdges.remove(item)
                   #  print("Path is", path)
                else:
                    
                    for i in range(len(path)):
                        for out in myEdges:
                            if out[0] == path[i]:
                                current = path[i]
                               # print("Current is", current)
                                nextItem = i + 1

    print("Your path is: ", path, "\n")

    # build sequence
    mySequence = ''
    for i in range(len(path)):
        if i == 0:
            mySequence += myVertices[path[i]]
        else:
            mySequence += myVertices[path[i]][-1]

    print("Your sequence is: ", mySequence)

main()
