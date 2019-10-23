#gofud gofudan cuyyy

total = 0
saldo = 1000

#array menu dan merchant
menu = [[16000, 20500, 14000, 13000],
        [24000, 15500, 18000, 30000],
        [16000, 13000, 16000, 17500]]


def RestaurantFind(i):
    tempat = ["Crisbar", "Salman", "Upnormal"]
    return tempat[i]
def Crisbar(j):
    crisbarr = ['Geprek Crispy','Geprek Tomat','Geprek Matah','Geprek Mozzarella']
    return crisbarr[j]
def Salman(k):
    salmann = ['Takol','Kuro','Go-Milk','Siomay']
    return salmann[k]
def Upno(l):
    upnoo = ['Si Eko','Roti Bakar','Cireng','Indomie']
    return upnoo[l]
print('GO-FOOD')
print()
print('Silahkan memilih merchant :')
print()
for i in range(3):
    print(RestaurantFind(i))
print()

#pilih merchant
merchant = int(input('Pilih merchant (Crisbar = 1, Salman = 2, Upnormal = 3) :'))
n = merchant - 1

print('Restaurant yang dipilih :'+RestaurantFind(merchant-1))
if merchant == 1:
    for m in range(4):
         print((m+1),'.',Crisbar(m),'=',menu[n][m])
    print()
elif merchant == 2:
    for m in range(4):
         print((m+1),'.',Salman(m),'=',menu[n][m])
    print()
elif merchant == 3:
    for m in range(4):
         print((m+1),'.',Upno(m),'=',menu[n][m])
    print()

selesai = False
while selesai == False:
    makan = int(input('Pilih makanan :'))
    m = makan - 1
    berapa = int(input('tentukan jumlah :'))
    total += (menu[n][m]*berapa)
    done = int(input('apakah anda ingin memilih lagi? (ya=1, tidak=0) : '))
    if done == 0:
        selesai = True
if merchant == 1:
    jarak = 5000
elif merchant == 2:
    jarak = 6000
elif merchant == 3:
    jarak = 7000
    
total += jarak*(4/1)

print('total biaya adalah =',total,' rupiah')

bayar = int(input('pilih metode pembayaran (cash=0, gopay=1) : '))
if bayar == 0:
    print('pesanan anda sedang diproses...')
elif bayar == 1:
    print('saldo gopay anda adalah ',saldo)
    if saldo >= total:
        cukup = True
    elif saldo < total:
        cukup = False
    if cukup == True:
        print('pesanan anda sedang diproses...')
        saldo -= total
        print('saldo anda sekarang :',saldo)
    elif saldo < total:
        while cukup == False:
            print('saldo anda tidak mencukupi, apakah anda ingin mengisi saldo?')
            isi = int(input('ya = 1, tidak = 0 :'))
            if isi == 1:
                isiy = int(input('isi saldo gopay anda :'))
                saldo += isiy
                print('saldo anda sekarang =',saldo)
                if saldo >= total:
                    print('saldo anda mencukupi, pesanan anda sedang diproses...')
                    saldo -= total
                    print()
                    print('saldo anda sekarang :',saldo)
                    cukup = True
            elif isi == 0:
                print('harap melakukan pembayaran menggunakan cash')
                cukup = True
                
