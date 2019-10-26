'''
DIRECTORY
| ARRAY DATA
    | loc[]             12
    | pos[]             22
    | street[]          32
| FUNGSI
    | distTo()          52
    | Jarak()           61
    | pickStreet()      x
'''
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
    [1, 4, 6],
    [3, 4, 5],
    [4, 6, 7],
    [1, 5, 5],
    [2, 3, 5],
    [2, 6, 7],
    [2, 5, 5]
]



###distTo()
'''
distTo(posA, posB)
parameter posA dan posB dapat berupa indeks loc[] ataupun indeks pos[]
'''
def distTo(A, B):
    dist = math.sqrt((pos[A][0]+pos[B][0])*(pos[A][0]+pos[B][0]) + (pos[A][1]+pos[B][1])*(pos[A][1]+pos[B][1]))
    return dist

###Jarak()
'''
jarak(asal, destinasi) 
parameter asal dan destinasi adalah indeks loc[]
'''
def Jarak(start, end):
    dist = 0 
    
    currentNode = start
    queue = ""

    while currentNode != end:
        queue += pickStreet(currentNode, end)


    return dist

###PICKSTREET MENCARI JALAN YANG TERHUBUNG DENGAN A DENGAN DISPLACEMENT TERKECIL DARI A KE B
def pickStreet(A, B):
    #Routes adalah indeks jalan yang terhubung dengan A
    routes = ""
    
    #RoutesEnd adalah ujung lainnya dari jalan yang terhubung dengan A
    routesEnd = ""

    #Count menghitung panjang string routes dan routesEnd
    count = 0

    for i in range(7):
        #Mencari jalan yang terhubung dengan A
        #Menambahkan indeksnya ke routes, dan menambahkan indeks jalan akhirnya ke routesEnd
        if street[i][0] == A:
            routes = routes + str(i)
            routesEnd = routesEnd + str(street[i][1])
            count += 1
        elif street[i][1] == A:
            routes += i
            routesEnd = routesEnd + str(street[i][0])
            count += 1

    #DEBUG
    print(routes)
    print(count) 
    print(routesEnd)

    for i in range(count):
        print(routes[i], routesEnd[i])
    
    return routesEnd

###minIndex()
'''
Menerima input array, indeks awal dan akhir daerah definisi yang diperiksa
'''
def minIndex(array, start, end):
    iminim = start
    for i in range(start, end+1):
        if array[i] < array[iminim]:
            iminim = i
    return iminim

###sortQueue()
'''
Menerima input suatu array(queue), mengurutkan dari nilai terkecil
'''
def sortQueue(queue):
    newQueue = [0 for i in range(queue[0]+1)]
    newQueue[0] = queue[0]
    len = queue[0]
    
    for i in range(1, len+1):
        newQueue[i] = queue[minIndex(queue, 1, len)]
        queue[minIndex(queue, 1, len)] = 99

    print(queue)

    return newQueue

###progressQueue()
'''
Menerima input suatu array(queue), menghilangkan indeks 1 dan memajukan seluruh indeks dibelakangnya
'''
def progressQueue(queue):
    newQueue = [0 for i in range(queue[0])]
    newQueue[0] = queue[0]-1
    print(queue)
    for i in range(1, queue[0]):
        newQueue[i] = queue[i+1]

    return newQueue



