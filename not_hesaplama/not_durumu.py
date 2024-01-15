import sys
import time

def anamenu ():
    ad=input("Adınız nedir?")
    vize=int(input("Lütfen vize notunuzu giriniz."))
    final=int(input("Lütfen final notunuzu giriniz."))
    proje=int(input("Lütfen proje notunuzu giriniz."))
    odev=int(input("Lütfen ödev notunuzu giriniz."))
    ortalama=(vize+final+proje+odev)/4
    print("╔═════════════════════╗")
    print("║   NOT HESAPLAYICI   ║")
    print("║                     ║")
    print("║ 1-Ortalama Hesaplama║")
    print("║ 2-Durum Bildirimi   ║")
    print("║ 3-Not Analizi       ║")
    print("║ 4-Ana Menü          ║")
    print("║ 5-Çıkış             ║")
    print("║                     ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        print("Ortalaman:",ortalama)
        anamenu()
    elif secim=="2":
        if ortalama<50:print("Kaldın")
        else:print("Geçtin")
        anamenu()
    elif secim=="3":
        if vize>85:print("Vizen çok güzel, vizedede aynı performansı sergile. AFERİN.")
        elif vize>70:print("Vizen güzel geçmiş anlaşılan.")
        elif vize>50:print("Vizeyi geçmişsin.")
        else:print("Vizeyi geçemedin ama üzülme belki finalde geçersin.")

        if final>85:print("Finalin çok güzel geçmiş anlaşılan. AFERİN.")
        elif final>70:print("Finalin güzel geçmiş anlaşılan.")
        elif final>50:print("Finali geçmişsin.")
        else:print("Finalde biraz çuvalladın.")

        if proje>85:print("Projeleri çok güzel yapmışsın anlaşılan. AFERİN.")
        elif proje>70:print("Projeleri güzel yapmışsın anlaşılan.")
        elif proje>50:print("Projeler tam öğretmenin istediği gibi değil anlaşılan ama geçmişsin.")
        else:print("Projelerden kalmışsın daha sıkı çalışman lazım.")

        if odev>85:print("Ödevlerini çok güzel yapmışsın anlaşılan. AFERİN.")
        elif odev>70:print("Ödevlerini güzel yapmışsın anlaşılan.")
        elif odev>50:print("Ödevlerin tam öğretmenin istediği gibi değil anlaşılan ama geçmişsin.")
        else:print("Ödevlerden kalmışsın daha sıkı çalışman lazım.")

        if ortalama>85:print("Sınıfı takdir alarak geçtin. TEBRİKLER.")
        elif ortalama>70:print("Sınıfı teşekkür alarak geçtin. TEBRİKLER.")
        elif ortalama>50:print("Sınıfı geçtin. TEBRİKLER.")
        else:print("Sınıfta kaldın, ama üzülme seneye daha sıkı çalışır geçersin geçemediklerini.")
        anamenu()
    elif secim=="4":
        print("Ana Menü'ye dönülüyor.")
        return
    elif secim=="5":
        print("Program 3 saniye içinde kapatılacak.")
        time.sleep(3)
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        anamenu()
