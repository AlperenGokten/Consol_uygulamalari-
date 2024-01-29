class Kayit:
    def __init__(self,gad,gsoyad,gtelefon="---"):
        self.ad = gad
        self.soyad = gsoyad
        self.telefon = gtelefon
    def __str__(self):
        return f"Kaydedilen: {self.ad} {self.soyad} {self.telefon}"
    
def menu():
    print ("╔════════════════════════╗")
    print ("║  REHBER PROGRAMI       ║")
    print ("╠════════════════════════╣")
    print ("║  1-Rehbere ekle        ║")
    print ("║  2-Kayıtları listele   ║")
    print ("║  3-Kayıt düzelt        ║")
    print ("║  4-Kayıt sil           ║")
    print ("║  5-Kayıt ara           ║")
    print ("║  6-Çıkış               ║")
    print ("║  Seçimizini giriniz    ║")
    print ("╚════════════════════════╝")
    secim = input ()
    if secim == "1": 
        rehbereEkle()
        listele()
        menu()
    if secim == "2": 
        listele()
        menu()
        
    if secim == "4": 
        sil()
        menu()
        
    if secim == "5": 
        ara()
        menu()

def ara():
    # dict, obje, json # yapı olarak aynı
    import ast
    kayit = {}
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    print (okunan)
    print("\nSatır satır")
    for a in okunan:
        kayit = ast.literal_eval(a)
        print (type(kayit))
        print(kayit)
        print(kayit["ad"])
    dosya.close()  
        
def rehbereEkle():
    dosya = open("rehber.txt","a")
    
   
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    telefon= input("Numara: ")
    yazilacak = {"ad":ad,"soyad":soyad,"numara":telefon}
    dosya.write(str(yazilacak)+"\n")
    
  

    dosya.close()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        kayit = {}
        for k in dosya.readlines():
            kayit = k
            print(k)
           
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()

def sil():
    pass

menu()


