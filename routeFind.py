import math


###DAFTAR NAMA DAN INDEKS TEMPAT
loc = [
    "Crisbar",
    "Salman",
    "Upnormal",
    "Tubis",
    "GKUB",
    "Boromeus"
]

###DAFTAR KOORDINAT LOKASI 
pos = [
    [5, 8],
    [4, 1],
    [7, 5],
    [11, 8],
    [1, 5],
    [11, 1]
]

###DAFTAR JALAN
'''
street[x][0] = titik awal jalan(indeks loc)
street[x][1] = titik akhir jalan(indeks loc)
street[x][2] = panjang jalan
'''
street = [
    [0, 3, 6],
    [2, 3, 5],
    [3, 5, 7],
    [0, 4, 5],
    [1, 2, 5],
    [1, 5, 7],
    [1, 4, 5]
]

numOfStreets = 7

def dist(asal, destinasi):
    dist = math.sqrt((pos[asal][0]-pos[destinasi][0])*(pos[asal][0]-pos[destinasi][0]) + (pos[asal][1]-pos[destinasi][1])*(pos[asal][1]-pos[destinasi][1]))
    return dist

def setMacet(timeOfDay):
    if timeOfDay == "Morning" or "1":
        street[2][2] *= 2.00
        street[0][2] *= 1.25
        street[1][2] *= 1.25
    elif timeOfDay == "Afternoon" or "2":
        street[1][2] *= 1.50
        street[4][2] *= 2.00
        street[2][2] *= 2.00
        street[1][2] *= 1.50
        street[4][2] *= 2.00
        street[2][2] *= 1.25
        street[1][2] *= 2.00

    elif timeOfDay == "Evening" or "3":
        street[5][2] *= 0.80
        street[0][2] *= 1.50
        street[1][2] *= 1.25


def Jarak(asal, destinasi):
    '''
    nodes relisted
    nodes[x][0] = heuretic distance
    nodes[x][1] = real distance
    nodes[x][2] = combined distance
    '''

    nodes = [
        [dist(0, destinasi), 0, 9999, 0],
        [dist(1, destinasi), 0, 9999, 0],
        [dist(2, destinasi), 0, 9999, 0],
        [dist(3, destinasi), 0, 9999, 0],
        [dist(4, destinasi), 0, 9999, 0],
        [dist(5, destinasi), 0, 9999, 0],
    ]
    currentNode = asal
    
    while currentNode != destinasi:
        count = connectedCount(currentNode)
        connectedNode = connectedNodes(currentNode)
        connectedStreet = connectedStreets(currentNode)

        for i in range(count):
            nodes = updateDist(nodes, int(connectedNode[i]), currentNode, int(connectedStreet[i]))
            nodes[int(connectedNode[i])][2] = nodes[int(connectedNode[i])][0] + nodes[int(connectedNode[i])][1] 

        nodes[currentNode][3] = 1
        currentNode = pickNextNode(nodes, currentNode)

    distance = nodes[currentNode][1]

    return distance

def connectedNodes(currentNode):
    nodes = ""
    for i in range(7):
        #Mencari jalan yang terhubung dengan A
        #Menambahkan indeksnya ke routes, dan menambahkan indeks jalan akhirnya ke routesEnd
        if street[i][0] == currentNode:
            nodes = nodes + str(street[i][1])
        elif street[i][1] == currentNode:
            nodes = nodes + str(street[i][0])

    return nodes

def connectedStreets(currentNode):
    streets = ""
    for i in range(numOfStreets):
        #Mencari jalan yang terhubung dengan A
        #Menambahkan indeksnya ke routes, dan menambahkan indeks jalan akhirnya ke routesEnd
        if street[i][0] == currentNode:
            streets = streets + str(i)
        elif street[i][1] == currentNode:
            streets = streets + str(i)

    return streets

def connectedCount(currentNode):
    count = 0
    for i in range(7):
        #Mencari jalan yang terhubung dengan A
        #Menambahkan indeksnya ke routes, dan menambahkan indeks jalan akhirnya ke routesEnd
        if street[i][0] == currentNode:
            count += 1
        elif street[i][1] == currentNode:
            count += 1
    
    return count

def updateDist(nodes, nextNode, originNode, path):
    currentDist = nodes[nextNode][1]
    newDist = nodes[originNode][1] + street[path][2]
    newnodes = nodes

    if currentDist == 0:
        newnodes[nextNode][1] = newDist
    else:
        if currentDist < newDist:
            newnodes[nextNode][1] = currentDist
        else:
            newnodes[nextNode][1] = newDist


    return newnodes

def pickNextNode(nodes, currentNode):
    if currentNode != 5:
        iminim = currentNode+1
    else:
        iminim = 4

    for i in range(6):
        if nodes[i][2] <= nodes[iminim][2] and nodes[i][3] == 0 and nodes[iminim][3] == 0:
            iminim = i
    
    return iminim

setMacet(1)
print(Jarak(0, 5))