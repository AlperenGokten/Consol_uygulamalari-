import takvis.takvim


def anamenu():   

    print("╔═══════════════════╗")
    print("║ 1-OYUNLAR         ║")
    print("║ 2-ŞEKİL ÇİZDİRME  ║")
    print("║ 3-TAKVİM          ║")
    print("║ 4-RİTMİK SAYMA    ║")
    print("║ 5-NOT HESAPLAMA   ║")
    print("╚═══════════════════╝")
    secim = input()

    if secim == "3" :
       takvis.takvim.takvimmenu()
       anamenu()

anamenu()




