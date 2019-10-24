#gofud gofudan cuyyy

total = 0
saldo = 1000

#array menu dan merchant
menu = [[16000, 20500, 14000, 13000],
        [24000, 15500, 18000, 30000],
        [16000, 13000, 16000, 17500]]

#array nama makanan
menu2 = [['Geprek Crispy','Geprek Tomat','Geprek Matah','Geprek Mozzarella'],
         ['Takol','Kuro','Go-Milk','Siomay'],
         ['Si Eko','Roti Bakar','Cireng','Indomie']]

#fungsi nama merchant
def RestaurantFind(i):
    tempat = ["Crisbar", "Salman", "Upnormal"]
    return tempat[i]
def DistFind():
    return 5000

#interface awal
print('GO-FOOD')
print()
print('Silahkan memilih merchant :')
for i in range(3):
    print(str(i+1)+'. '+RestaurantFind(i))
print()

#pilih merchant
merchant = int(input('Pilih merchant : '))
n = merchant - 1

#display menu dari merchant yang telah dipilih
print('Restaurant yang dipilih :'+RestaurantFind(merchant-1))
for i in range(4):
    print(str(i+1)+'. '+str(menu2[n][i])+': '+str(menu[n][i]))

selesai = False
while selesai == False:
    makan = int(input('Pilih makanan :'))
    m = makan - 1

#menentukan jumlah makanan yang ingin dipesan
    berapa = int(input('Tentukan jumlah :'))
    total += (menu[n][m]*berapa)
    done = int(input('Apakah anda ingin memilih lagi? (ya=0, tidak=1) :'))
    if done == 1:
        selesai = True
print()

#menambahkan total biaya dengan biaya pengiriman
total += DistFind()*(4/1)
print('Biaya makanan anda adalah = ',str(total-DistFind()*(4/1)))
print('Biaya antar anda adalah = ',str(DistFind()*(4/1)))
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
                
