from models import Harcama
from services import HarcamaYoneticisi
from file_manager import harcamalari_kaydet, harcamalari_yukle
from analysis import analiz_menu

yonetici = HarcamaYoneticisi()
yonetici.harcamalar = harcamalari_yukle()



while True:
    print("\n----HARCAMA TAKİP----")
    print("1- Harcama ekle")
    print("2- Harcamalari listele")
    print("3- Toplam harcamayi göster")
    print("4- Kategoriye göre ara")
    print("5- Analiz")
    print("6- Çikis")

    secim = input("Seçiminiz: ")

    
    if secim == "1":

        tarih = input("Tarih: ")
        kategori = input("Kategori: ")

        if kategori == "":
            print("Kategori boş bırakılamaz.")
            continue

        aciklama = input("Açıklama: ")

        try:
            tutar = float(input("Tutar: "))
        except ValueError:
            print("Geçersiz tutar girdiniz.")
            continue

        harcama = Harcama(
            tarih,
            kategori,
            aciklama,
            tutar
        )

        yonetici.harcama_ekle(harcama)
        harcamalari_kaydet(yonetici.harcamalar)

        print("Harcama başarıyla eklendi.")


    elif secim == "2":
        yonetici.harcamalari_listele()

    elif secim == "3":
        yonetici.toplam_harcama()

    elif secim == "4":
        yonetici.kategoriye_gore_ara()

    elif secim == "5":
         analiz_menu(yonetici.harcamalar)

    elif secim == "6":
        print("programdan cikis yapiliyor..")
        break

    else:
        print("Lütfen geçerli bir seçim yapınız.")