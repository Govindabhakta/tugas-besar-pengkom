
###BayarGopay()
'''
gopay = variabel untuk pembayaran (integer)
harga = variabel yang didapatkan dari gofood atau goTransport (integer)
asumsi user tidak salah input
'''
def BayarGopay(gopay, harga):
    # Inisialisasi variabel
    payWithGopay = 0
    payWithCash = 0
    
    if gopay >= harga:
        # Gopay cukup untuk membayar
        payWithGopay = harga
        # payWithGopay memiliki nilai sebesar harga
        print("Pay ",payWithGopay," with Gopay, ")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    elif gopay < harga:
        # Gopay tidak cukup untuk membayar
        payWithCash = harga - gopay
        # payWIthCash adalah sisa biaya yang harus dibayar dengan cash
        payWithGopay = gopay
        print("Pay ",payWithGopay," with Gopay + ", payWithCash," with Cash")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    
    if Bayar == "Y":
        # User ingin melakukan pembayaran
        if gopay >= harga:
            '''
            Gopay cukup untuk membayar
            gopay berkurang karena bayar gofood atau goTransport
            '''
            gopay = gopay - harga
        elif gopay < harga:
            '''
            Gopay tidak cukup untuk membayar
            gopay menjadi 0
            '''
            gopay = 0
    return
        

