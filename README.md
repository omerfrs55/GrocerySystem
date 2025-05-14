# GrocerySystem

Market ve Depo Otomasyon Sistemi
Türkçe Açıklama
Özellikler
Müşteri, Admin ve Kasiyer Menüsü
Müşteri Kaydı ve Girişi
Alışveriş ve Bakiye Yönetimi
Kupon Sistemi
Stok ve Ürün Yönetimi
Depo Yerleşimi ve Kısa Yol Algoritması
Ürün Çürüme/SKT Takibi
Denetim ve Hırsızlık Kontrolü
Mini Oyun ve Skor Tablosu
Satış İstatistikleri ve Raporlama
Kurulum
Python 3 yüklü olmalı.
Proje klasöründe aşağıdaki dosyaları oluşturun:
customerRegister.txt
adminRegister.txt
scoreboard.txt
stockproducts.txt
coupons.txt
customerPurchases.txt
Dosya formatları için örnekler aşağıdadır.
Kullanım
Terminalde çalıştırmak için:
Apply to Grocery.py
Run
Fonksiyonlar ve Açıklamaları
Genel Akış
ana_menu()
Uygulamanın ana menüsüdür. Kullanıcıdan rol seçimi alır ve ilgili menüye yönlendirir.
kasiyer_menu()
Yeni müşteri kaydı yapılmasını sağlar.
musteri_giris_menu()
Müşteri girişi için kullanıcı adı ve şifre ister.
admin_giris_menu()
Admin girişi için kullanıcı adı ve şifre ister.
Müşteri Fonksiyonları
musteri_menu(kullanici_adi)
Giriş yapan müşterinin alışveriş, kupon, bakiye, geçmiş, mini oyun gibi işlemleri seçmesini sağlar.
musteri_alisveris_menu(kullanici_adi)
Ürün seçimi, stok kontrolü, kupon kullanımı, bakiye düşümü ve alışveriş kaydı işlemlerini yapar.
musteri_kupon_goruntule(kullanici_adi)
Müşterinin sahip olduğu kuponları listeler.
musteri_bakiye_yukle(kullanici_adi)
Müşterinin bakiyesine para ekler.
musteri_alisveris_gecmisi(kullanici_adi)
Müşterinin yaptığı alışverişleri listeler.
Mini Oyun
musteri_minigame_menu(kullanici_adi)
Müşteri, market temalı taş-kağıt-makas oyununu oynayabilir veya skor tablosunu görebilir.
musteri_minigame_oyna(kullanici_adi)
Elma > Muz, Muz > Portakal, Portakal > Elma kurallarıyla oynanır. Kazanırsa skor artar ve kupon kazanabilir.
skor_guncelle(kullanici_adi, sonuc)
Kullanıcının skorunu günceller ve son oyun tarihini kaydeder.
musteri_minigame_scoreboard()
Tüm kullanıcıların skorlarını ve son oyun tarihlerini listeler.
Kupon Sistemi
Kuponlar coupons.txt dosyasında tutulur.
Alışveriş sırasında kuponu olan müşteriye indirim uygulanır ve kupon kullanıldıktan sonra silinir.
Admin, müşterilere manuel olarak da kupon tanımlayabilir.
Stok ve Ürün Yönetimi
admin_stok_goruntule_guncelle()
Stokları listeler ve istenirse stok miktarını günceller.
admin_toptanci_siparis()
Toptancıdan ürün siparişi verir, admin bakiyesinden düşer ve stoklara ekler.
Depo Yerleşimi ve Kısa Yol Algoritması
admin_depo_yerlesim()
Depodaki ürünlerin 5x5 matris üzerinde yerleşimini gösterir.
admin_depo_kisayol()
Depo girişinden (0,0) ilgili ürünün koordinatına Manhattan algoritması ile en kısa yolu adım adım gösterir.
Ürün Çürüme/SKT Takibi
admin_urun_curume_takip()
Stoktaki ürünlerin son kullanma tarihlerini kontrol eder, süresi geçenleri ve 5 günden az kalanları uyarır.
Denetim ve Hırsızlık Kontrolü
admin_denetim_hirsizlik()
Stok ve satış verilerini karşılaştırır, hash algoritması ile veri bütünlüğü kontrolü yapar, eksik/hatalı durumları bildirir.
Satış İstatistikleri
admin_satis_istatistik()
En çok satılan ürünleri ve miktarlarını listeler.
Algoritmalar ve Özel Kodlar
Manhattan Shortest Path:
Depoda bir ürünün yerine en kısa yol, sadece yukarı/aşağı/sağa/sola hareketle bulunur.
Kullanımı: admin_depo_kisayol()
Hashing:
Stok ve satış miktarlarının bütünlüğünü kontrol etmek için MD5 hash kullanılır.
Kullanımı: admin_denetim_hirsizlik()
Minigame:
Basit bir taş-kağıt-makas algoritması, skor ve kupon ödülleriyle birlikte.
Kullanımı: musteri_minigame_oyna() ve skor_guncelle()
English Description
Features
Customer, Admin, and Cashier Menus
Customer Registration and Login
Shopping and Balance Management
Coupon System
Stock and Product Management
Warehouse Layout and Shortest Path Algorithm
Product Expiry/Decay Tracking
Audit and Theft Control
Minigame and Scoreboard
Sales Statistics and Reporting
Installation
Python 3 must be installed.
Create the following files in the project directory:
customerRegister.txt
adminRegister.txt
scoreboard.txt
stockproducts.txt
coupons.txt
customerPurchases.txt
See below for file format examples.
Usage
To run in terminal:
Apply to Grocery.py
Run
Functions and Explanations
General Flow
ana_menu()
The main menu of the application. Gets user role selection and redirects to the relevant menu.
kasiyer_menu()
Allows new customer registration.
musteri_giris_menu()
Asks for username and password for customer login.
admin_giris_menu()
Asks for username and password for admin login.
Customer Functions
musteri_menu(kullanici_adi)
Allows the logged-in customer to select shopping, coupons, balance, history, minigame, etc.
musteri_alisveris_menu(kullanici_adi)
Handles product selection, stock check, coupon usage, balance deduction, and purchase recording.
musteri_kupon_goruntule(kullanici_adi)
Lists the coupons owned by the customer.
musteri_bakiye_yukle(kullanici_adi)
Adds money to the customer's balance.
musteri_alisveris_gecmisi(kullanici_adi)
Lists the purchases made by the customer.
Minigame
musteri_minigame_menu(kullanici_adi)
The customer can play a market-themed rock-paper-scissors game or view the scoreboard.
musteri_minigame_oyna(kullanici_adi)
Played with Apple > Banana, Banana > Orange, Orange > Apple rules. If the customer wins, their score increases and they may win a coupon.
skor_guncelle(kullanici_adi, sonuc)
Updates the user's score and records the last game date.
musteri_minigame_scoreboard()
Lists all users' scores and last game dates.
Coupon System
Coupons are stored in coupons.txt.
If the customer has a coupon during shopping, a discount is applied and the coupon is deleted after use.
Admin can also manually assign coupons to customers.
Stock and Product Management
admin_stok_goruntule_guncelle()
Lists stocks and allows updating stock amounts.
admin_toptanci_siparis()
Orders products from wholesaler, deducts from admin balance, and adds to stock.
Warehouse Layout and Shortest Path Algorithm
admin_depo_yerlesim()
Shows the placement of products in a 5x5 warehouse matrix.
admin_depo_kisayol()
Shows the shortest path from warehouse entrance (0,0) to product location using Manhattan algorithm.
Product Expiry/Decay Tracking
admin_urun_curume_takip()
Checks expiry dates of products in stock, warns for expired or soon-to-expire products.
Audit and Theft Control
admin_denetim_hirsizlik()
Compares stock and sales data, uses hash algorithm for data integrity, reports missing or incorrect situations.
Sales Statistics
admin_satis_istatistik()
Lists the most sold products and their quantities.
Algorithms and Special Code Sections
Manhattan Shortest Path:
Finds the shortest path to a product in the warehouse using only up/down/left/right moves.
Used in: admin_depo_kisayol()
Hashing:
Uses MD5 hash to check the integrity of stock and sales amounts.
Used in: admin_denetim_hirsizlik()
Minigame:
Simple rock-paper-scissors algorithm with score and coupon rewards.
Used in: musteri_minigame_oyna() and skor_guncelle()
Lisans / License
Bu proje eğitim amaçlıdır.
This project is for educational purposes.
İletişim / Contact
Her türlü soru ve öneri için:
For any questions or suggestions:
your-email@example.com
