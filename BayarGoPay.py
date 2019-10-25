
###BayarGopay()
'''
gopay = variabel untuk pembayaran (integer)
harga = variabel yang didapatkan dari gofood atau goTransport (integer)
asumsi user tidak salah input
'''
def BayarGopay(gopay, harga):
    #Inisialisasi variable
    payWithGopay = 0
    payWithCash = 0
    
    if gopay >= harga:
        #Gopay cukup untuk membayar
        payWithGopay = harga
        print("Pay ",payWithGopay," with Gopay, ")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    elif gopay < harga:
        #Gopay tidak cukup untuk membayar
        payWithCash = harga - gopay
        payWithGopay = gopay
        print("Pay ",payWithGopay," with Gopay + ", payWithCash," with Cash")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    
    if Bayar == "Y":
        if gopay >= harga:
            gopay = gopay - harga
        elif gopay < harga:
            gopay = 0
    return
        

