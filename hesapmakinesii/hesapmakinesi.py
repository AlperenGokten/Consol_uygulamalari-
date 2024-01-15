import sys
import time

def anamenu():
    print("╔══════════════════╗")
    print("║  HESAP MAKİNESİ  ║")
    print("║                  ║")
    print("║ 1-Toplama (+)    ║")
    print("║ 2-Çıkarma (-)    ║")
    print("║ 3-Çarpma  (*)    ║")
    print("║ 4-Bölme   (/)    ║")
    print("║ 5-Üst Alma       ║")
    print("║ 6-Tam Bölme      ║")
    print("║ 7-Bütün işlemler ║")
    print("║ 8-Ana Menü       ║")
    print("║ 9-Çıkış          ║")
    print("║                  ║")
    print("╚══════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1+sayi2)
        anamenu()
    elif secim=="2":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1-sayi2)
        anamenu()
    elif secim=="3":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1*sayi2)
        anamenu()
    elif secim=="4":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1/sayi2)
        anamenu()
    elif secim=="5":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1**sayi2)
        anamenu()
    elif secim=="6":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1//sayi2)
        anamenu()
    elif secim=="7":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("İki sayının toplamı:",sayi1+sayi2)
        print("İki sayının farkı:",sayi1-sayi2)
        print("İki sayının çarpımı:",sayi1*sayi2)
        print("İki sayının bölümü:",sayi1/sayi2)
        print("İki sayının üstü:",sayi1**sayi2)
        print("İki sayının tam bölümü:",sayi1//sayi2)
        anamenu()
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
