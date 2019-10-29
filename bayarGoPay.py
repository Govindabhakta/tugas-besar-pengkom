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
        gopay = gopay - payWithGopay
    else:
        print("Yauds lain kali ae\n")
    
    done = input("Enter buat cabuts balik ke halaman utama yo")
    return gopay
        

