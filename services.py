class HarcamaYoneticisi:

    def __init__(self):
        self.harcamalar = []

    def harcama_ekle(self, harcama):
        self.harcamalar.append(harcama)

    def harcamalari_listele(self):
        if not self.harcamalar:
            print("Henüz harcama bulunmuyor.")
            return

        for sira, harcama in enumerate(self.harcamalar, start=1):
            print(
                sira,
                "|",
                harcama.tarih,
                "|",
                harcama.kategori,
                "|",
                harcama.aciklama,
                "|",
                harcama.tutar,
                "TL"
            )

    def toplam_harcama(self):

        if not self.harcamalar:
            print("Henüz harcama bulunmuyor.")
            return

        toplam = 0

        for harcama in self.harcamalar:
            toplam += harcama.tutar

        print("Toplam harcama:", toplam, "TL")

    def kategoriye_gore_ara(self):

        kategori = input("Aramak istediğiniz kategori: ")

        bulunanlar = []

        for harcama in self.harcamalar:
            if harcama.kategori.lower() == kategori.lower():
                bulunanlar.append(harcama)

        if not bulunanlar:
            print("Bu kategoriye ait harcama bulunamadı.")
            return

        print("\n===== KATEGORİ SONUÇLARI =====")

        toplam = 0

        for harcama in bulunanlar:
            print(
                harcama.tarih,
                "|",
                harcama.kategori,
                "|",
                harcama.aciklama,
                "|",
                harcama.tutar,
                "TL"
            )

            toplam += harcama.tutar

        print("Kategori toplamı:", toplam, "TL")