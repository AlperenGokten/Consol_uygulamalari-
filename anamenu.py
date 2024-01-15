import takvis.takvim
import hesapmakinesii.hesapmakinesi

def anamenu():   

    print("╔═══════════════════╗")
    print("║ 1-OYUNLAR         ║")
    print("║ 2-ŞEKİL ÇİZDİRME  ║")
    print("║ 3-TAKVİM          ║")
    print("║ 4-RİTMİK SAYMA    ║")
    print("║ 5-NOT HESAPLAMA   ║")
    print("║ 6-İDEAL KİLO      ║")
    print("║   HESAPLAMA       ║")
    print("║ 7-ÇARPIM TABLOSU  ║")
    print("║ 8-SINIF LİSTESİ   ║")
    print("║ 9-HESAP MAKİNASI  ║")
    print("║ 10-DÖVİZ UYGULAMAS║")
    print("╚═══════════════════╝")
    secim = input()
    if secim == "3" :
       takvis.takvim.takvimmenu()
       anamenu()
    if secim == "9" :
       python.hesapmakinesi.hesapmenu()
       anamenu()
 
anamenu()
