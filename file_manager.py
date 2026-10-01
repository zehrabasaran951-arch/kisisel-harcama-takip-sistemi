import csv
from models import Harcama


def harcamalari_kaydet(harcamalar):
    with open("harcamalar.csv", "w", newline="", encoding="utf-8") as dosya:

        writer = csv.writer(dosya)

        writer.writerow([
            "tarih",
            "kategori",
            "aciklama",
            "tutar"
        ])

        for harcama in harcamalar:
            writer.writerow([
                harcama.tarih,
                harcama.kategori,
                harcama.aciklama,
                harcama.tutar
            ])


def harcamalari_yukle():
    harcamalar = []

    try:
        with open("harcamalar.csv", "r", newline="", encoding="utf-8") as dosya:

            reader = csv.DictReader(dosya)

            for satir in reader:

                harcama = Harcama(
                    satir["tarih"],
                    satir["kategori"],
                    satir["aciklama"],
                    float(satir["tutar"])
                )

                harcamalar.append(harcama)

    except FileNotFoundError:
        pass

    return harcamalar