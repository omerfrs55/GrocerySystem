# 🛒 Grocery System (Market Sistemi)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

## 📋 İçindekiler
- [Proje Hakkında](#-proje-hakkında)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Veri Yapıları ve Algoritmalar](#-veri-yapıları-ve-algoritmalar)
- [Güvenlik](#-güvenlik)
- [Oyun Mantığı](#-oyun-mantığı)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)

## 🎯 Proje Hakkında
Bu proje, bir market yönetim sistemi simülasyonudur. Müşteri ve yönetici arayüzleri, stok takibi, kupon sistemi ve mini oyun özellikleri içerir.

## 🛠 Kullanılan Teknolojiler
- **Python 3.x**: Ana programlama dili
- **cryptography**: Şifreleme işlemleri için
- **datetime**: Tarih/saat işlemleri için
- **os**: Terminal temizleme işlemleri için

## 📊 Veri Yapıları ve Algoritmalar

### Dictionary (Sözlük) Kullanımı
```python
dosya_dict = {
    'customer': 'customerRegister.txt',
    'admin': 'adminRegister.txt',
    'scoreboard': 'scoreboard.txt',
    'stock': 'stockproducts.txt',
    'coupons': 'coupons.txt',
    'purchases': 'customerPurchases.txt'
}
```
- **Kullanım Amacı**: Dosya yollarını organize etmek ve yönetmek
- **Avantajları**: 
  - Kolay erişim
  - Merkezi yönetim
  - Kod tekrarını önleme

### Minimax Algoritması
```python
def minimax(self, depth, is_maximizing):
    if self.check_winner():
        if self.winner == '🍎':
            return -1
        elif self.winner == '🍌':
            return 1
        else:
            return 0
```
- **Kullanım Yeri**: Tic-tac-toe oyununda bilgisayar hamlesi
- **Amacı**: En iyi hamleyi seçmek
- **Çalışma Mantığı**: 
  - Derinlik öncelikli arama
  - Olası tüm hamleleri değerlendirme
  - En iyi sonucu seçme

### Majority Vote (Çoğunluk Oylaması)
```python
sirali = sorted(urun_sayac.items(), key=lambda x: x[1], reverse=True)
```
- **Kullanım Yeri**: En çok satılan ürünleri belirleme
- **Amacı**: Ürün popülerliğini ölçme
- **İşleyiş**: 
  - Satış sayılarını toplama
  - Büyükten küçüğe sıralama
  - Sıralama bilgisini stok dosyasına kaydetme

### TimeSort
```python
skor_listesi.sort(key=lambda x: x[1], reverse=True)
```
- **Kullanım Yeri**: Skor tablosu sıralaması
- **Amacı**: Skorları büyükten küçüğe sıralama
- **Özellikler**: 
  - Python'un yerleşik sıralama algoritması
  - O(n log n) karmaşıklık

## 🔒 Güvenlik

### Cryptography Kullanımı
```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
```
- **Kullanım Amacı**: Kullanıcı şifrelerini güvenli şekilde saklama
- **Özellikler**:
  - Simetrik şifreleme
  - Güvenli anahtar üretimi
  - Şifreli veri saklama

## 🎮 Oyun Mantığı

### Class Yapısı
```python
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = '🍎'
        self.winner = None
        self.game_over = False
```
- **Kullanım Amacı**: Tic-tac-toe oyununu yönetme
- **Özellikler**:
  - Oyun tahtası yönetimi
  - Oyuncu sırası takibi
  - Kazanan kontrolü
  - Oyun durumu yönetimi

## 💻 Kurulum

1. Python 3.x'i yükleyin
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install cryptography
```
3. Projeyi klonlayın:
```bash
git clone https://github.com/kullanici/grocery-system.git
```

## 🚀 Kullanım

1. Programı başlatın:
```bash
python Grocery.py
```

2. Menüden seçim yapın:
   - Müşteri Menüsü
   - Yönetici Menüsü

### Müşteri Özellikleri
- Alışveriş yapma
- Kupon kullanma
- Mini oyun oynama
- Skor tablosunu görüntüleme

### Yönetici Özellikleri
- Stok yönetimi
- En çok satılan ürünleri görüntüleme
- Çürüme takibi

## 📝 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
