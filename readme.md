\# Kişisel Harcama Takip ve Analiz Sistemi



Python kullanılarak geliştirilen, kullanıcıların günlük harcamalarını kaydetmesini, listelemesini ve farklı yöntemlerle analiz etmesini sağlayan konsol tabanlı bir harcama takip uygulamasıdır.



\## Projenin Amacı



Bu projenin amacı, Python'da öğrendiğim:



\- Nesne yönelimli programlama (OOP)

\- Modüler programlama

\- CSV dosya işlemleri

\- NumPy

\- Pandas

\- Veri filtreleme ve gruplama



konularını gerçek bir proje üzerinde uygulamaktır.



\## Özellikler



\### Harcama İşlemleri



\- Yeni harcama ekleme

\- Harcamaları listeleme

\- Toplam harcamayı hesaplama

\- Kategoriye göre harcama arama

\- Harcamaları CSV dosyasına kaydetme

\- Program açıldığında kayıtlı harcamaları tekrar yükleme



\### Analiz Özellikleri



\- Genel istatistikler

\- CSV verilerini görüntüleme

\- Kategori bazında toplam harcama

\- En fazla harcama yapılan kategoriyi bulma

\- Belirli bir tutarın üzerindeki harcamaları filtreleme

\- Aylık harcama raporu



\## Kullanılan Teknolojiler



\- Python

\- NumPy

\- Pandas

\- CSV

\- Nesne Yönelimli Programlama (OOP)



\## Proje Yapısı



```text

kisisel\_harcama\_takip\_sistemi/

│

├── main.py

├── models.py

├── services.py

├── file\_manager.py

├── analysis.py

├── .gitignore

└── README.md

```



\### Dosyaların Görevleri



\*\*main.py\*\*



Programın başlangıç noktasıdır. Ana menüyü oluşturur ve kullanıcı seçimlerini yönetir.



\*\*models.py\*\*



`Harcama` sınıfını içerir. Bir harcamaya ait tarih, kategori, açıklama ve tutar bilgilerini temsil eder.



\*\*services.py\*\*



`HarcamaYoneticisi` sınıfını içerir. Harcama ekleme, listeleme, toplam harcama ve kategoriye göre arama gibi işlemleri yönetir.



\*\*file\_manager.py\*\*



Harcamaların `harcamalar.csv` dosyasına kaydedilmesini ve program başladığında tekrar okunmasını sağlar.



\*\*analysis.py\*\*



NumPy ve Pandas kullanılarak harcamalar üzerinde istatistiksel ve kategorik analizlerin yapılmasını sağlar.



\## Kurulum



Projeyi bilgisayarınıza indirdikten sonra proje klasöründe terminali açın.



Gerekli kütüphaneleri yüklemek için:



```bash

py -m pip install numpy pandas

```



\## Çalıştırma



Proje klasöründe terminali açın ve:



```bash

py main.py

```



komutunu çalıştırın.



Program açıldığında aşağıdaki menü görüntülenir:



```text

\---- HARCAMA TAKİP ----

1- Harcama ekle

2- Harcamaları listele

3- Toplam harcamayı göster

4- Kategoriye göre ara

5- Analiz

6- Çıkış

```



`5 - Analiz` seçeneği ile analiz menüsüne ulaşılabilir.



\## Veri Saklama



Harcama kayıtları `harcamalar.csv` dosyasında tutulur.



CSV dosyasının temel yapısı:



```text

tarih,kategori,aciklama,tutar

```



`harcamalar.csv` dosyası `.gitignore` içerisinde tutulduğu için kullanıcıya ait harcama verileri GitHub'a yüklenmez.



\## Öğrenme Kazanımları



Bu proje geliştirilirken Python'da:



\- Sınıf ve nesne kullanımı

\- Metot oluşturma

\- Modüller arası bağlantı

\- Dosya okuma ve yazma

\- CSV ile veri saklama

\- NumPy ile sayısal analiz

\- Pandas DataFrame kullanımı

\- `groupby()` ile kategori analizi

\- Veri filtreleme

\- Tarih verileriyle çalışma



konularında pratik yapılmıştır.



\## Geliştirme Fikirleri



Projeye ilerleyen aşamalarda:



\- Grafiklerle veri görselleştirme

\- Gelir-gider takibi

\- Bütçe belirleme

\- Daha gelişmiş aylık/yıllık raporlar

\- Kullanıcı arayüzü



gibi özellikler eklenebilir.

