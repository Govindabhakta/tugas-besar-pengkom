import bayarGoPay
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
locnum = [
    1,
    2,
    3,
    4,
    5,
    6,
]

#fungsi untuk meminta user memilih posisi pickup dan delivery
def pick():
    print("lokasi penjemputan dan pengantaran: ")
    for i in range (6):
        print(locnum[i], ". ", loc[i])

    destinasi = input("Silakan pilih destinasi: ")

    asal = input("silakan pilih lokasi penjemputan: ")
    return destinasi, asal

def dat():
    sname = input("Nama pengirim: ")
    snum = input("No. HP pengirim: ")
    rname = input("Nama penerima: ")
    rnum = input("No. HP penerima: ")

def DistFind():
    return 25

def price(destinasi, asal, tarif):
    if asal == "1" or asal == "Crisbar" or asal == "crisbar":
        if destinasi == "2" or destinasi == "Salman" or destinasi == "salman":
            total = DistFind()*tarif
        elif destinasi == "3" or destinasi == "Uprnomal" or destinasi == "upnormal":
            total = DistFind()*tarif
        elif destinasi == "4" or destinasi == "Tubis" or destinasi == "tubis":
            total = DistFind()*tarif
        elif destinasi == "5" or destinasi == "GKUB" or destinasi == "gkub":
            total = DistFind()*tarif
        elif destinasi == "6" or destinasi == "Boromeus" or destinasi == "boromeus":
            total = DistFind()*tarif
    elif asal == "2" or asal == "Salman" or asal == "salman":
        if destinasi == "1" or destinasi == "Crisbar" or destinasi == "crisbar":
            total = DistFind() * tarif
        elif destinasi == "3" or destinasi == "Uprnomal" or destinasi == "upnormal":
            total = DistFind() * tarif
        elif destinasi == "4" or destinasi == "Tubis" or destinasi == "tubis":
            total = DistFind() * tarif
        elif destinasi == "5" or destinasi == "GKUB" or destinasi == "gkub":
            total = DistFind() * tarif
        elif destinasi == "6" or destinasi == "Boromeus" or destinasi == "boromeus":
            total = DistFind() * tarif
    elif asal == "3" or asal == "Upnormal" or asal == "upnormal":
        if destinasi == "1" or destinasi == "Crisbar" or destinasi == "crisbar":
            total = DistFind() * tarif
        elif destinasi == "2" or destinasi == "Salman" or destinasi == "salman":
            total = DistFind() * tarif
        elif destinasi == "4" or destinasi == "Tubis" or destinasi == "tubis":
            total = DistFind() * tarif
        elif destinasi == "5" or destinasi == "GKUB" or destinasi == "gkub":
            total = DistFind() * tarif
        elif destinasi == "6" or destinasi == "Boromeus" or destinasi == "boromeus":
            total = DistFind() * tarif
    elif asal == "4" or asal == "Tubis" or asal == "tubis":
        if destinasi == "1" or destinasi == "Crisbar" or destinasi == "crisbar":
            total = DistFind() * tarif
        elif destinasi == "2" or destinasi == "Salman" or destinasi == "salman":
            total = DistFind() * tarif
        elif destinasi == "3" or destinasi == "Upnormal" or destinasi == "upnormal":
            total = DistFind() * tarif
        elif destinasi == "5" or destinasi == "GKUB" or destinasi == "gkub":
            total = DistFind() * tarif
        elif destinasi == "6" or destinasi == "Boromeus" or destinasi == "boromeus":
            total = DistFind() * tarif
    elif asal == "5" or asal == "GKUB" or asal == "gkub":
        if destinasi == "1" or destinasi == "Crisbar" or destinasi == "crisbar":
            total = DistFind() * tarif
        elif destinasi == "2" or destinasi == "Salman" or destinasi == "salman":
            total = DistFind() * tarif
        elif destinasi == "3" or destinasi == "Upnormal" or destinasi == "upnormal":
            total = DistFind() * tarif
        elif destinasi == "4" or destinasi == "Tubis" or destinasi == "tubis":
            total = DistFind() * tarif
        elif destinasi == "6" or destinasi == "Boromeus" or destinasi == "boromeus":
            total = DistFind() * tarif
    elif asal == "6" or asal == "Boromeus" or asal == "boromeus":
        if destinasi == "1" or destinasi == "Crisbar" or destinasi == "crisbar":
            total = DistFind() * tarif
        elif destinasi == "2" or destinasi == "Salman" or destinasi == "salman":
            total = DistFind() * tarif
        elif destinasi == "3" or destinasi == "Upnormal" or destinasi == "upnormal":
            total = DistFind() * tarif
        elif destinasi == "4" or destinasi == "Tubis" or destinasi == "tubis":
            total = DistFind() * tarif
        elif destinasi == "5" or destinasi == "GKUB" or destinasi == "gkub":
            total = DistFind() * tarif
    return total

def Goride():
    destinasi, asal = pick()
    total = price(destinasi, asal ,4000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    BayarGopay(100000, total)

def Gocar():
    destinasi, asal = pick()
    total = price(destinasi, asal, 8000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    BayarGopay(100000, total)

def Gosend():
    destinasi, asal = pick()
    dat()
    total = price(destinasi, asal ,4000)
    print("Harga penggunaan jasa: ", total, " Rupiah")
    BayarGopay(100000, total)

def BayarGopay(gopay, harga):
    payWithGopay = 0
    payWithCash = 0

    if gopay >= harga:
        payWithGopay = harga
        payWithCash = 0

    if gopay < harga:
        payWithCash = harga - gopay
        payWithGopay = gopay

    print("Pay ", payWithGopay, " with Gopay, ", payWithCash, " with Cash")
    print("Bayar?")
    print("(jawaban antara (Bayar) atau (Tidak Bayar)")
    Bayar = input()
    if Bayar == Bayar:
        if gopay >= harga:
            gopay = gopay - harga
        elif gopay < harga:
            gopay = 0
    return

jasa = [
    "GoRide",
    "GoCar",
    "GoSend"
]

print("Jasa yang tersedia:")
for i in range (3):
    print(jasa[i])
jasa = input("Pilih Jasa yang akan digunakan: ")

if jasa == "GoRide":
    Goride()
elif jasa == "GoCar":
    Gocar()
elif jasa == "GoSend":
    Gosend()
else:
    print("Silakan ulangi pengisian dengan benar")