from bayarGoPay import BayarGopay
from routeFind import Jarak, Location

def price(destinasi, asal, tarif):
    total = 0
    total = Jarak(asal, destinasi)*tarif
    return total

#fungsi untuk meminta user memilih posisi pickup dan delivery
def pick():
    print("lokasi penjemputan dan pengantaran: ")

    loc = Location()
    for i in range (6):
        print("[",i+1, "]", loc[i])

    destinasi   = int(input("Silakan pilih destinasi: "))
    asal        = int(input("silakan pilih lokasi penjemputan: "))
    return destinasi-1, asal-1

def Goride(gopay):
    destinasi, asal = pick()
    total = price(destinasi, asal ,4000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    gopay = BayarGopay(gopay, total)
    return gopay

def Gocar(gopay):
    destinasi, asal = pick()
    total = price(destinasi, asal, 8000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    gopay = BayarGopay(gopay, total)
    return gopay

def Gosend(gopay):
    destinasi, asal = pick()
    dat()
    total = price(destinasi, asal ,4000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    gopay = BayarGopay(gopay, total)
    return gopay

def dat():
    sname   = input("Nama pengirim: ")
    snum    = input("No. HP pengirim: ")
    rname   = input("Nama penerima: ")
    rnum    = input("No. HP penerima: ")

jasa = [
    "GoRide",
    "GoCar",
    "GoSend"
]

# print("Jasa yang tersedia:")
# for i in range (3):
#     print(jasa[i])
# jasa = input("Pilih Jasa yang akan digunakan: ")

# if jasa == "GoRide":
#     Goride(gopay)
# elif jasa == "GoCar":
#     Gocar()
# elif jasa == "GoSend":
#     Gosend()
# else:
#     print("Silakan ulangi pengisian dengan benar")