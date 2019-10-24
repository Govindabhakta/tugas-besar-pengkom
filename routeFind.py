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
###street[nomor jalan][A]
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
    
    return dist

'''
up for revisi
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
    
    return
'''


