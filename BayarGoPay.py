
###BayarGopay()
'''
gopay = variabel untuk pembayaran (integer)
harga = variabel yang didapatkan dari gofood atau goTransport (integer)
asumsi user tidak salah input
'''
def BayarGopay(gopay, harga):
    payWithGopay = 0
    payWithCash = 0
    
    if gopay >= harga:
        payWithGopay = harga
        print("Pay ",payWithGopay," with Gopay, ")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    elif gopay < harga:
        payWithCash = harga - gopay
        payWithGopay = gopay
        print("Pay ",payWithGopay," with Gopay + ", payWithCash," with Cash")
        print("Bayar?")
        print("(jawaban (Y) untuk bayar dan (N) untuk tidak bayar)")
        Bayar = input()
    
    if Bayar == Y:
        if gopay >= harga:
            gopay = gopay - harga
        elif gopay < harga:
            gopay = 0
    return
        

