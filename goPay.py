'''
gopay =  variabel untuk pembayaran (integer)
gopay_Plus = variabel untuk nilai penambahan gopay (integer)
asumsi tidak salah input 
'''
def TopUpGopay(gopay):
    print("Instruksi Pengisian Saldo Gopay")
    print("Metode Pembelian Saldo Gopay")
    print("1. Instan")
    print("2. Instruksi")
    i = int(input("Pilih Metode Pembelian: "))
    if i == 1:
        print("ISI NOMINAL")
        gopay_Plus = int(input())
        print("Jumlah Top up             Rp", gopay_Plus)
        print("Biaya GO-PAY              Rp 1000")
        print("------------------------------------")
        print("Total Pembayaran          Rp", gopay_Plus+1000)
        print("Masukkan PIN")
        PIN = int(input())
        gopay = gopay + gopay_Plus
        return (gopay)
    
    if i == 2:
        print("1. Driver Gojek")
        print("   Minta driver kamu untuk isi GoPay. Bebas Biaya Admin!")
        print("2. Minimarket & Pegadaian")
        print("   Di Minimarket dan Pegadaian mana pun terdekat.")
        print("3. BCA OneKlik")
        print("   Praktis dan aman isi saldo pakai kartu debit BCA kamu.")
        print("4. Mobile Banking")
        print("   Kapan pun, di mana pun cukup lewat aplikasi di HP-mu.")
        print("5. SMS Banking")
        print("   Gak ada internet? Pakai SMS banking tetap bisa!")
        print()
        Pil_Met = int(input("Pilih Metode Pembelian Saldo Gopay: "))
        print()
        if (Pil_Met == 1):
            print("Cara meminta driver transfer Gopay:")
            print("BIAYA ADMIN GRATIS! - TANPA MINIMUM ISI")
            print()
            print("1. Buat pesanan di GoRide, GoCar, GoFood, atau GoSend.")
            print("2. Bilang ke driver yang sedang mengambil order kalau kamu mau ditransferin GoPay.")
            print("3. Kasih ke driver yang tunai sejumlah GoPay yang ditransfer ke kamu.")
            print("4. Pastikan GoPay kamu sudah bertambah.")
            return

        elif (Pil_Met == 2):
            print("Minimarket & Pegadaian")
            print("1. Alfamart")
            print("2. Alfamidi")
            print("3. Dan+Dan")
            print("4. Lawson")
            print("5. Pegadaian")
            print()
            Pil_Mart = int(input("Pilih Minimarket atau Pegadaian: "))
            if (Pil_Mart == 1):
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp2.000 - MINIMUM ISI Rp20.000")
                print()
                print("1. Minta bantuan kasir untuk mengisi GoPay.")
                print("2. Beritahu nomor HP yang kamu pakai di aplikasi Gojek.")
                print("3. Beritahu nominal isi GoPay.")
                print("4. Biaya nominal yang ingin kamu isi ke kasir (plus biaya admin Rp.2000).")
                print("5. Kasir akan mengisi saldo ke akun GoPay kamu.")
                print("6. Pastikan GoPay kamu sudah bertambah.")
                print("7. SImpan tanda terimanya sebagai bukti pembayaran sah.")
                return
            else:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp2.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Minta bantuan kasir untuk mengisi GoPay.")
                print("2. Beritahu nomor HP yang kamu pakai di aplikasi Gojek.")
                print("3. Beritahu nominal isi GoPay.")
                print("4. Biaya nominal yang ingin kamu isi ke kasir (plus biaya admin Rp.2000).")
                print("5. Kasir akan mengisi saldo ke akun GoPay kamu.")
                print("6. Pastikan GoPay kamu sudah bertambah.")
                print("7. SImpan tanda terimanya sebagai bukti pembayaran sah.")
                return

        elif (Pil_Met == 3):
            print("Cara isi GoPay:")
            print("BIAYA ADMIN Rp1.000 - TANPA MINIMUM ISI")
            print()
            print("1. Pilih Isi Saldo lalu pilih tab Instan.")
            print("2. Masukkin jumlah GoPay yang mau diisi.")
            print("3. Pilih kartu BCA yang mau dipakai atau tambah kartu baru.")
            print("4. Klik LANJUT.")
            print("5. Konfirmasi pembayaranmu lalu pilih KONFIRMASI & BAYAR.")
            print("6. Masukkan PIN GoPay kamu.")
            print("7. Setelah berhasil isi saldo, kamu bakal dapat notifikasi kalau GoPay kamu udah bertambah.")
            return
        
        elif (Pil_Met == 4):
            print("Mobile banking")
            print("1. BCA")
            print("2. Mandiri")
            print("3. BRI")
            print("4. BNI")
            print("5. PermataBank")
            print()
            i = int(input("Pilih Banknya:"))
            if i == 1:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Login ke m-BCA.")
                print("2. Pilih M-TRANSFER > TRNASFER BCA VIRTUAL ACCOUNT.")
                print("3. Masukkan kode perusahaan untuk Gojek: 70001 dan nomor HP yang terdaftar pada aplikasi Gojek")
                print("   (contoh: 7000108XXXXXXXXXX).")
                print("4. Masukkan jumlah GoPay yang ingin diisi.")
                print("5. Masukkan PIN m-BCA kamu.")
                print("6. Ikuti petunjuk selanjutnya untuk menyelesaikan proses pengisian GoPay.")
                return
            
            elif i == 2:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp15.000")
                print()
                print("1. Login ke Mandiri Mobile Application.")
                print("2. Pilih Bayar > Buat Pembayaran Baru > Multipayment > GoPay Customer.")
                print("3. Masukkan nomor telepon yang terdaftar pada aplikasi Gojek.")
                print("4. Masukkan jumlah GoPay yang ingin diisi.")
                print("5. Ikuti petunjuk selanjutnya untuk menyelesaikan proses pengisian GoPay.")
                return
            
            elif i == 3:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Login ke Mobile Banking BRI.")
                print("2. Pilih ISI ULANG > GoPay > JENIS TRANSAKSI > 301341-COSTUMER.")
                print("3. Masukkan nomor HP yang terdaftar pada aplikasi Gojek.")
                print("4. Masukkan jumlah GoPay yang ingin diisi.")
                print("5. Masukkan PIN untuk memverifikasi transaksi.")
                print("6. Ikuti petunjuk selanjutnya untuk menyelesaikan proses pengisian GoPay.")
                return
            
            elif i == 4:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Buka ke BNI SMS Banking.")
                print("2. Pilih TRANSFER > TOP UP GoPay > GoPay CUSTOMER.")
                print("3. Masukkan nomor HP Anda yang terdaftar pada Gojek.")
                print("4. Masukkan jumlah top up yang diinginkan.")
                print("5. Ikuti instruksi untuk menyelesaikan transaksi.")
                return
            
            else:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Login ke PermataMobile.")
                print("2. Pilih menu ISI ULANG > ISI ULANG Gojek.")
                print("3. Pilih Rekening ANda.")
                print("4. Masukkan nomor HP Anda yang terdaftar pada Gojek.")
                print("5. Masukkan jumlah top up yang diinginkan.")
                print("6. Ikuti instruksi untuk menyelesaikan transaksi.")
                return
            
        else:
            print("SMS Banking")
            print("1. BRI")
            print("2. BNI")
            i = int(input("Pilih Banknya: "))
            if i == 1:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Kirim SMS ke 3300 dan ketik: BELI(spasi)GOPAY(spasi)301341(spasi)Nomor Handphone(spasi)Nominal(spasi)PIN(spasi)Mobile Banking.")
                print("2. Ikuti petunjuk selanjutnya untuk menyelesaikan proses pengisian GoPay.")
                return
            
            else:
                print("Cara isi GoPay:")
                print("BIAYA ADMIN Rp1.000 - MINIMUM ISI Rp10.000")
                print()
                print("1. Kirim SMS ke 3346 dan ketik: TOP(spasi)GOPAY(spasi)CUSTOMER(spasi)Phone Number(spasi)TopUp Amount.")
                print("2. Ikuti petunjuk selanjutnya untuk menyelesaikan proses pengisian GoPay.")
                return
