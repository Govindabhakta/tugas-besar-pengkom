#gofud gofudan cuyyy

total = 0
saldo = 1000

#print menu dan merchant
menu = [[16000, 20500, 14000, 13000],
        [24000, 15500, 18000, 30000],
        [16000, 13000, 16000, 17500]]


'''
Bikin dia print nama restoran dulu, baru menunya
Pakai placeholder RestaurantFind() yang ada di main.py
'''

for i in range (3):
    for j in range (4):
        print(menu[i][j],'', end='')
    print()

#pilih merchant
merchant = int(input('pilih merchant : '))
n = merchant - 1
selesai = False
while selesai == False:
    makan = int(input('pilih makanan :'))
    m = makan - 1
    berapa = int(input('tentukan jumlah :'))
    total += (menu[n][m]*berapa)
    done = int(input('apakah anda ingin memilih lagi? (ya=1, tidak=0) : '))
    if done == 0:
        selesai = True

'''
Buat cari jarak, pakai placeholder yang ada di main.py
'''
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
    '''
    Buar bayar pakai gopay, pakai placeholder BayarGopay() yang di main.py
    '''
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
                    print('pesanan anda sedang diproses...')
                    saldo -= total
                    print('saldo anda sekarang :',saldo)
                    cukup = True
            elif isi == 0:
                print('harap melakukan pembayaran menggunakan cash')
                cukup = True
                
