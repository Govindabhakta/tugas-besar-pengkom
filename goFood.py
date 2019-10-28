#gofud gofudan cuyyy
from bayarGoPay import BayarGopay
from routeFind import Jarak, Location

total = 0
saldo = 1000

def goFood(gopay):
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
        jumlah = int(input('Tentukan jumlah :'))
        totalBayar = 0
        totalBayar += (menu[n][m]*jumlah)
        done = str(input('Apakah anda ingin memilih lagi? (Y/N) :'))
        if done == "N":
            selesai = True
        elif done == "Y":
            selesai = False
    print()

    #Input tujuan pengiriman
    listTujuan = Location()
    print("Nearby...")
    for i in range(len(listTujuan)):
        print("[", i+1, "]", listTujuan[i])
    
    #Input indeks tujuan pengiriman 
    tujuan = int(input("Delivery location index: "))-1    
    #Ongkos kirim adalah 1250/km
    ongkos = 1250

    biayaAntar = Jarak(n, tujuan)*ongkos
    totalBayar += biayaAntar

    print('Biaya makanan = ', totalBayar - biayaAntar) 
    print('Biaya antar   = ', biayaAntar)
    BayarGopay(gopay, totalBayar) 
    return

                