# 🛒 Market ve Depo Otomasyon Sistemi

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</div>


  <p><em>Python tabanlı terminal uygulaması | Eğitim amaçlı proje</em></p>

---

## 📌 Türkçe Açıklama

### 🎯 Özellikler

<ul>
  <li>Müşteri, Admin ve Kasiyer Menüsü</li>
  <li>Müşteri Kaydı ve Girişi</li>
  <li>Alışveriş ve Bakiye Yönetimi</li>
  <li>Kupon Sistemi</li>
  <li>Stok ve Ürün Yönetimi</li>
  <li>Depo Yerleşimi ve Kısa Yol Algoritması</li>
  <li>Ürün Çürüme / SKT Takibi</li>
  <li>Denetim ve Hırsızlık Kontrolü</li>
  <li>Mini Oyun ve Skor Tablosu</li>
  <li>Satış İstatistikleri ve Raporlama</li>
</ul>

---

### ⚙️ Kurulum

<ul>
  <li>Python 3 yüklü olmalı.</li>
  <li>Proje klasöründe aşağıdaki dosyalar oluşturulmalı:</li>
</ul>

```
customerRegister.txt  
adminRegister.txt  
scoreboard.txt  
stockproducts.txt  
coupons.txt  
customerPurchases.txt
```

---

### ▶️ Kullanım

Terminalde çalıştırmak için:

```
python Grocery.py
```

---

## 🔧 Fonksiyonlar ve Açıklamaları

### 🔁 Genel Akış

- **ana_menu()** – Rol seçimi ve yönlendirme menüsü  
- **kasiyer_menu()** – Yeni müşteri kaydı  
- **musteri_giris_menu()** – Müşteri girişi  
- **admin_giris_menu()** – Admin girişi

### 👤 Müşteri Fonksiyonları

- **musteri_menu(kullanici_adi)** – Ana müşteri işlemleri menüsü  
- **musteri_alisveris_menu(kullanici_adi)** – Ürün seçimi, kupon, bakiye ve alışveriş kaydı  
- **musteri_kupon_goruntule(kullanici_adi)** – Kupon görüntüleme  
- **musteri_bakiye_yukle(kullanici_adi)** – Bakiye yükleme  
- **musteri_alisveris_gecmisi(kullanici_adi)** – Alışveriş geçmişi görüntüleme

### 🎮 Mini Oyun

- **musteri_minigame_menu(kullanici_adi)** – Oyun ve skor tablosu  
- **musteri_minigame_oyna(kullanici_adi)** – Elma > Muz, Muz > Portakal, Portakal > Elma  
- **skor_guncelle(kullanici_adi, sonuc)** – Skor güncelleme  
- **musteri_minigame_scoreboard()** – Skor tablosu görüntüleme

### 🎫 Kupon Sistemi

- Kuponlar `coupons.txt` dosyasında saklanır  
- Alışveriş sırasında indirim sağlar  
- Kullanıldıktan sonra sistemden silinir  
- Admin manuel olarak kupon tanımlayabilir

### 📦 Stok ve Ürün Yönetimi

- **admin_stok_goruntule_guncelle()** – Stok görüntüleme ve güncelleme  
- **admin_toptanci_siparis()** – Toptancıdan ürün siparişi

### 🗺️ Depo Yerleşimi ve Kısa Yol

- **admin_depo_yerlesim()** – 5x5 matris yerleşimi  
- **admin_depo_kisayol()** – Manhattan algoritması ile en kısa yol

### 🧪 Ürün Çürüme/SKT Takibi

- **admin_urun_curume_takip()** – SKT kontrolü ve uyarılar

### 🕵️‍♂️ Denetim ve Hırsızlık Kontrolü

- **admin_denetim_hirsizlik()** – Stok ve satış verilerinin MD5 hash ile karşılaştırılması

### 📊 Satış İstatistikleri

- **admin_satis_istatistik()** – En çok satılan ürünler ve miktarları

---

## 🧠 Algoritmalar ve Özel Kodlar

### ➡️ Manhattan Shortest Path

- Depodaki ürüne en kısa yolu bulur  
- Yalnızca yukarı/aşağı/sağa/sola hareket izni  
- Kullanım: `admin_depo_kisayol()`

### 🔐 Hashing (MD5)

- Stok ve satış verilerinin bütünlüğünü sağlar  
- Kullanım: `admin_denetim_hirsizlik()`

### 🎯 Minigame

- Elma > Muz, Muz > Portakal, Portakal > Elma  
- Skor güncellemesi ve kupon ödülleri  
- Kullanım: `musteri_minigame_oyna()` ve `skor_guncelle()`

---

## 🌐 English Description

<details>
<summary>Click to expand</summary>

### Features

- Customer, Admin, and Cashier Menus  
- Customer Registration and Login  
- Shopping and Balance Management  
- Coupon System  
- Stock and Product Management  
- Warehouse Layout and Shortest Path Algorithm  
- Product Expiry/Decay Tracking  
- Audit and Theft Control  
- Minigame and Scoreboard  
- Sales Statistics and Reporting  

### Installation

- Python 3 must be installed  
- Create the following files:

```
customerRegister.txt  
adminRegister.txt  
scoreboard.txt  
stockproducts.txt  
coupons.txt  
customerPurchases.txt
```

### Usage

To run in terminal:
```
python Grocery.py
```

</details>

---

## 📝 Lisans / License

Bu proje eğitim amaçlıdır.  
This project is for educational purposes only.

---

## 📬 PROJE SAHİPLERİ:

PROJE SAHİPLERİ:  
ÖMER FARUK SAĞLAM
SAMET ERDOĞAN

---

<div align="center">
  <strong>Teşekkürler! / Thank You!</strong>  
</div>
