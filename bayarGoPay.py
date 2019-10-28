def BayarGopay(gopay, harga):
    payWithGopay = 0
    payWithCash = 0
    
    if gopay >= harga:
        payWithGopay = harga
        payWithCash = 0
        
    if gopay < harga:
        payWithCash = harga - gopay
        payWithGopay = gopay
        
    print("Pay ",payWithGopay," with Gopay, ", payWithCash," with Cash")
    print("Bayar? (Y/N)")
    Bayar = str(input())
    if Bayar == "Y":
        print("Okii pembayaran lunas...\n")
        if gopay >= harga:
            gopay = gopay - harga
        elif gopay < harga:
            gopay = 0
    return
        

