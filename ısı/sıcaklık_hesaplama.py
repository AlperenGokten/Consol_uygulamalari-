import sys
import time

def anamenu():
    print("╔═══════════════════════════════╗")
    print("║       SICAKLIK ÇEVİRME        ║")
    print("║                               ║")
    print("║ 1- Celsius(°C) Fahrenheit(°F) ║")
    print("║    Çevirici                   ║")
    print("║ 2- Fahrenheit(°F) Celsius(°C) ║")
    print("║    Çevirici                   ║")
    print("║ 3- Celsius(°C) Kelvin (K)     ║")
    print("║    Çevirici                   ║")
    print("║ 4- Kelvin(K) Celsius(°C)      ║")
    print("║    Çevirici                   ║")
    print("║ 5- Fahrenheit(°F) Kelvin(K)   ║")
    print("║    Çevirici                   ║")
    print("║ 6- Kelvin(K) Fahrenheit(°F)   ║")
    print("║    Çevirici                   ║")
    print("║ 7- Sıcaklık Değeri            ║")
    print("║    Karşılaştırma              ║")
    print("║ 8- Ana Menü                   ║")
    print("║ 9- Çıkış                      ║")
    print("║                               ║")
    print("╚═══════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        Celsius=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Fahrenheit=(1.8*Celsius)+32
        print(f"{Celsius} Celsius(°C) {Fahrenheit} Fahrenheit(°F) eder.")
        sicaklik_menu()
    elif secim=="2":
        Fahrenheit=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Celsius=(Fahrenheit-32)/1.8
        print(f"{Fahrenheit} Fahrenheit(°F) {Celsius} Celsius(°C) eder.")
        sicaklik_menu()
    elif secim=="3":
        Celsius=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Kelvin=Celsius+273.15
        print(f"{Celsius} Celsius(°C) {Kelvin} Kelvin(K) eder.")
        sicaklik_menu()
    elif secim=="4":
        Kelvin=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Celsius=Kelvin-273.15
        print(f"{Kelvin} Kelvin(K) {Celsius} Celsius(°C) eder.")
        sicaklik_menu()
    elif secim=="5":
        Fahrenheit=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Kelvin=((Fahrenheit-32)/1.8)+273.15
        print(f"{Fahrenheit} Fahrenheit(°F) {Kelvin} Kelvin(K) eder.")
        sicaklik_menu()
    elif secim=="6":
        Kelvin=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Fahrenheit=((Kelvin-273.15)*9/5)+32
        print(f"{Kelvin} Kelvin(K) {Fahrenheit} Fahrenheit (°F) eder.")
        sicaklik_menu()
    elif secim=="7":
        sicaklik1=int(input("Lütfen birinci sıcaklığı giriniz:"))
        sicaklik2=int(input("Lütfen ikinci sıcaklığı giriniz:"))
        if sicaklik1>sicaklik2:
            print("Sıcaklık fazladır.")
        elif sicaklik1<sicaklik2:
            print("Sıcaklık azdır.")
        else:
            print("Sıcaklıklar eşittir.")
    elif secim=="8":
        print("Ana Menü'ye dönülüyor.")
        return
    elif secim=="9":
        print("Program 3 saniye içinde kapatılacak.")
        time.sleep(3)
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        anamenu()
