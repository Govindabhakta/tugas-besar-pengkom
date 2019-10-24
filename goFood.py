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
def DistFind():
    return 25000

print('GO-FOOD')
print()
print('Silahkan memilih merchant :')
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
    berapa = int(input('Tentukan jumlah :'))
    total += (menu[n][m]*berapa)
    done = int(input('Apakah anda ingin memilih lagi? (ya=1, tidak=0) :'))
    if done == 0:
        selesai = True

total += DistFind()*(4/1)

print('Total biaya adalah =',total,' rupiah')
print()
bayar = int(input('Pilih metode pembayaran (cash=0, go-pay=1) : '))
if bayar == 0:
    print('Pesanan anda sedang diproses...')
elif bayar == 1:
    print('Saldo gopay anda adalah ',saldo)
    if saldo >= total:
        cukup = True
    elif saldo < total:
        cukup = False
    if cukup == True:
        print('Pesanan anda sedang diproses...')
        saldo -= total
        print('Saldo anda sekarang :',saldo)
    elif saldo < total:
        while cukup == False:
            print('Saldo anda tidak mencukupi, apakah anda ingin mengisi saldo?')
            isi = int(input('ya = 1, tidak = 0 :'))
            if isi == 1:
                isiy = int(input('Isi saldo gopay anda :'))
                saldo += isiy
                print('Saldo anda sekarang =',saldo)
                if saldo >= total:
                    print('Saldo anda mencukupi, pesanan anda sedang diproses...')
                    saldo -= total
                    print()
                    print('Saldo anda sekarang :',saldo)
                    cukup = True
            elif isi == 0:
                print('Harap melakukan pembayaran menggunakan cash')
                cukup = True
                
