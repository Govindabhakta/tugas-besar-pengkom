'''
TUGAS BESAR PENGENALAN KOMPUTASI
Dosen: Dr. Rahadian Yusuf, S.T.,M.T.
SIMULASI APLIKASI GOJEK

I Gede Govindabhakta        16519020
Ryandito Diandaru           16519150
Kevin Angga Yumawan         16519210
Aindrea Rayhan Supriyanto   16519360
'''
from gofood import goFood
from bayarGoPay import BayarGopay
from goPay import TopUpGopay
from goTransport import Gocar, Goride, Gosend

import os

###MAIN APPLICATION
def Gojek():
    gopay = 0

    appRunning = True
    print("Welcome to KojeG...")
    while appRunning:
        print("Saldo gopay ente:", gopay)
        print("[1] GoFood")
        print("[2] GoRide")
        print("[3] GoCar")
        print("[4] GoSend")
        print("[5] Topup Gopay")
        print("[6] Exit")

        mainMenuInput = int(input("Whatchu wanna do: "))
        os.system('cls')

        if mainMenuInput == 1:
            goFood(gopay)
        elif mainMenuInput == 2:
            Goride(gopay)
        elif mainMenuInput == 3:
            Gocar(gopay)
        elif mainMenuInput == 4:
            Gosend(gopay)
        elif mainMenuInput == 5:
            gopay = TopUpGopay(gopay)
        elif mainMenuInput == 6:
            appRunning = False
        
        if mainMenuInput != 6: 
            os.system('cls')
            print("Welcome back to KojeG...")

    print("Goodbye brudah")

    return
###END OF MAIN APPLICATION

Gojek()