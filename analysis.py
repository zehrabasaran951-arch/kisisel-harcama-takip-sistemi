import numpy as np
import pandas as pd 


def analiz_yap(harcamalar):

    if not harcamalar:
        print("Analiz yapılacak harcama bulunmuyor.")
        return

    tutarlar = np.array([
        harcama.tutar
        for harcama in harcamalar
    ])

    print("\n===== İSTATİSTİKLER =====")

    print("Toplam Harcama:", np.sum(tutarlar), "TL")
    print("Ortalama Harcama:", round(np.mean(tutarlar), 2), "TL")
    print("En Küçük Harcama:", np.min(tutarlar), "TL")
    print("En Büyük Harcama:", np.max(tutarlar), "TL")
    print("Standart Sapma:", round(np.std(tutarlar), 2))

def csv_oku():

    df = pd.read_csv("harcamalar.csv")  ## CSV'yi DataFrame'e çevirdik

    print(df)   ## dataFrame 

    return df

def kategori_analizi():
    df = pd.read_csv("harcamalar.csv")

    kategori_toplamlari = df.groupby("kategori")["tutar"].sum()
    ## .groupby("kategori") Harcamaları kategorilerine göre gruplandır
    ## Kategorilere göre grupla, tutarları seç ve her grubun toplamını hesapla.

    print("\n---KATEGORİ ANALİZİ---")
    print(kategori_toplamlari)


def en_cok_harcama_kategorisi():

    df = pd.read_csv("harcamalar.csv")

    kategori_toplamlari= df.groupby("kategori")["tutar"].sum()

    en_fazla_kategori = kategori_toplamlari.idxmax()  ## idxmax() → en büyük değerin hangi kategoriye ait olduğunu bulur.
    en_fazla_tutar = kategori_toplamlari.max()

    print("\n===== EN ÇOK HARCAMA YAPILAN KATEGORİ =====")
    print("En fazla harcama yapılan kategori:")
    print(en_fazla_kategori)
    print()
    print("Toplam:", en_fazla_tutar, "TL")


def harcama_filtrele():
    df = pd.read_csv("harcamalar.csv")

    minimum_tutar = float(input("minimum tutar:"))

    filtrelenmis = df[df["tutar"] >= minimum_tutar]

    print(f"\n{minimum_tutar} tl ve uzerindeki harcamalar")
    print(filtrelenmis[["aciklama", "tutar"]])

def aylik_rapor():
    df = pd.read_csv("harcamalar.csv")

    ay =input("ay seciniz:").strip().lower()

    df["tarih"] = pd.to_datetime(df["tarih"])

    aylar = {
        "ocak": 1,
        "şubat": 2,
        "mart": 3,
        "nisan": 4,
        "mayis": 5,
        "haziran": 6,
        "temmuz": 7,
        "ağustos": 8,
        "eylül": 9,
        "ekim": 10,
        "kasim": 11,
        "aralik": 12
    }

    if ay not in aylar:
        print("gecersiz ay")
        return

    secilen_ay= df[df["tarih"].dt.month == aylar[ay]]

    if secilen_ay.empty:
        print("bu aya ait harcama bulunmuyor")
        return

    toplam = secilen_ay["tutar"].sum()

    kategori_toplamlari = secilen_ay.groupby("kategori")["tutar"].sum()
    en_fazla_kategori = kategori_toplamlari.idxmax()

    ortalama = secilen_ay["tutar"].mean()
    en_yuksek = secilen_ay["tutar"].max()
    islem_sayisi = len(secilen_ay)

    print(f"\n===== {ay.upper()} RAPORU =====")
    print()
    print("Toplam Harcama:", round(toplam, 2), "TL")
    print()
    print("En fazla harcanan kategori:")
    print(en_fazla_kategori)
    print()
    print("Ortalama işlem:", round(ortalama, 2), "TL")
    print()
    print("En yüksek harcama:", en_yuksek, "TL")
    print()
    print("İşlem sayısı:", islem_sayisi)


def analiz_menu(harcamalar):

    while True:

        print("\n===== ANALİZ MENÜSÜ =====")
        print("1 - Genel İstatistikler")
        print("2 - CSV Verilerini Göster")
        print("3 - Kategori Analizi")
        print("4 - En Çok Harcama Yapılan Kategori")
        print("5 - Belirli Tutarın Üzerindeki Harcamalar")
        print("6 - Aylık Rapor")
        print("0 - Geri Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            analiz_yap(harcamalar)

        elif secim == "2":
            csv_oku()

        elif secim == "3":
            kategori_analizi()

        elif secim == "4":
            en_cok_harcama_kategorisi()

        elif secim == "5":
            harcama_filtrele()

        elif secim == "6":
            aylik_rapor()

        elif secim == "0":
            break

        else:
            print("Lütfen geçerli bir seçim yapınız.")