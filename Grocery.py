# Grocery System and Storage Main File  # Main file for the grocery system
# Market Sistemi ve Depolama Ana Dosyası  # Turkish title

# Files dictionary for .txt files  # EN: Dictionary for file paths // TR: Dosya yolları için sözlük
# .txt dosyaları için dosya sözlüğü  # EN: Turkish explanation // TR: Türkçe açıklama
dosya_dict = {
    'customer': 'customerRegister.txt',  # Customer info file
    'admin': 'adminRegister.txt',        # Admin info file
    'scoreboard': 'scoreboard.txt',      # Game scores file
    'stock': 'stockproducts.txt',        # Stock info file
    'coupons': 'coupons.txt',            # Coupons file
    'purchases': 'customerPurchases.txt' # Customer purchases file
}

# Main menu function  # EN: Main menu function // TR: Ana menü fonksiyonu
# Ana menü fonksiyonu  # EN: Turkish explanation // TR: Türkçe açıklama
def ana_menu():
    print("\n--- Grocery System and Storage ---")  # Print main title
    print("1. Cashier Menu (Kasiyer Menüsü)")  # Print cashier menu option
    print("2. Customer Menu (Müşteri Menüsü)")  # Print customer menu option
    print("3. Admin/Boss Menu (Yönetici/Patron Menüsü)")  # Print admin menu option
    print("0. Exit (Çıkış)")  # Print exit option
    secim = input("Select an option (Bir seçenek seçin): ")  # Get menu selection
    if secim == '1':
        kasiyer_menu()  # Go to cashier menu
    elif secim == '2':
        musteri_giris_menu()  # Go to customer login menu
    elif secim == '3':
        admin_giris_menu()  # Go to admin login menu
    elif secim == '0':
        print("Exiting... / Çıkılıyor...")  # Print exit message
    else:
        print("Invalid selection! / Geçersiz seçim!")  # Print invalid selection
        ana_menu()  # Show menu again

# Cashier menu (for customer registration)  # EN: Cashier menu function // TR: Kasiyer menüsü fonksiyonu
# Kasiyer menüsü (müşteri kaydı için)  # EN: Turkish explanation // TR: Türkçe açıklama
def kasiyer_menu():
    print("\n--- Cashier Menu / Kasiyer Menüsü ---")  # Print cashier menu title
    print("1. Register Customer (Müşteri Kaydı)")  # Print register customer option
    print("0. Back (Geri)")  # Print back option
    secim = input("Select an option (Bir seçenek seçin): ")  # Get menu selection
    if secim == '1':
        musteri_kayit()  # Go to customer registration
    elif secim == '0':
        ana_menu()  # Go back to main menu
    else:
        print("Invalid selection! / Geçersiz seçim!")  # Print invalid selection
        kasiyer_menu()  # Show cashier menu again

# Customer registration function  # EN: Customer registration function // TR: Müşteri kayıt fonksiyonu
# Müşteri kayıt fonksiyonu  # EN: Turkish explanation // TR: Türkçe açıklama
def musteri_kayit():
    print("\n--- Customer Registration / Müşteri Kaydı ---")  # Print registration title
    ad = input("Name (Ad): ")  # Get name
    soyad = input("Surname (Soyad): ")  # Get surname
    kullanici_adi = input("Username (Kullanıcı Adı): ")  # Get username
    sifre = input("Password (Şifre): ")  # Get password
    bakiye = '0'  # New customers start with 0 balance
    # Check if username exists / Kullanıcı adı var mı kontrol et  # EN: Check if username exists // TR: Kullanıcı adı var mı kontrol et
    with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
        satirlar = f.readlines()  # EN: Read all lines // TR: Tüm satırları oku
    var_mi = False  # EN: Username exists flag // TR: Kullanıcı var mı bayrağı
    for satir in satirlar:
        bilgiler = satir.strip().split(',')  # EN: Split by comma // TR: Virgül ile ayır
        if len(bilgiler) > 2 and bilgiler[2] == kullanici_adi:
            var_mi = True  # EN: Set exists flag // TR: Bayrağı true yap
    if var_mi:
        print("This username is already taken! / Bu kullanıcı adı zaten alınmış!")  # EN: Username taken message // TR: Kullanıcı adı alınmış mesajı
        kasiyer_menu()  # EN: Go back to cashier menu // TR: Kasiyer menüsüne dön
    else:
        # Save new customer with balance / Yeni müşteriyi bakiyesiyle kaydet  # EN: Save new customer // TR: Yeni müşteriyi kaydet
        with open(dosya_dict['customer'], 'a', encoding='utf-8') as f:
            f.write(ad + ',' + soyad + ',' + kullanici_adi + ',' + sifre + ',' + bakiye + '\n')  # EN: Write customer info // TR: Müşteri bilgisini yaz
        print("Customer registered successfully! / Müşteri başarıyla kaydedildi!")  # EN: Registration success // TR: Kayıt başarılı
        kasiyer_menu()  # EN: Go back to cashier menu // TR: Kasiyer menüsüne dön

# Customer login menu
# Müşteri giriş menüsü
def musteri_giris_menu():
    print("\n--- Customer Login / Müşteri Girişi ---")  # Print customer login title
    kullanici_adi = input("Username (Kullanıcı Adı): ")  # Get username
    sifre = input("Password (Şifre): ")  # Get password
    with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
        satirlar = f.readlines()  # Read all customer lines
    giris_basarili = False  # Login success flag
    for satir in satirlar:
        bilgiler = satir.strip().split(',')  # Split by comma
        if len(bilgiler) > 3 and bilgiler[2] == kullanici_adi and bilgiler[3] == sifre:
            giris_basarili = True  # Set login success
    if giris_basarili:
        print("Login successful! / Giriş başarılı!")  # Print login success
        musteri_menu(kullanici_adi)  # Go to customer menu
    else:
        print("Wrong username or password! / Hatalı kullanıcı adı veya şifre!")  # Print wrong login
        ana_menu()  # Go back to main menu

# Customer menu (to be developed)
# Müşteri menüsü (geliştirilecek)
def musteri_menu(kullanici_adi):  # EN: Customer menu for logged-in user // TR: Giriş yapan müşteri için menü
    print(f"\n--- Customer Menu for {kullanici_adi} / {kullanici_adi} için Müşteri Menüsü ---")  # EN: Print menu title // TR: Menü başlığını yazdır
    print("1. Shopping (Alışveriş)")  # EN: Shopping option // TR: Alışveriş seçeneği
    print("2. Coupons (Kuponlar)")  # EN: Coupons option // TR: Kuponlar seçeneği
    print("3. Minigame (Mini Oyun)")  # EN: Minigame option // TR: Mini oyun seçeneği
    print("4. Add Balance (Bakiye Yükle)")  # EN: Add balance option // TR: Bakiye yükleme seçeneği
    print("5. Purchase History (Alışveriş Geçmişi)")  # EN: Purchase history option // TR: Alışveriş geçmişi seçeneği
    print("6. Minigame Scoreboard (Mini Oyun Skor Tablosu)")  # EN: Minigame scoreboard option // TR: Mini oyun skor tablosu seçeneği
    print("0. Back (Geri)")  # EN: Back option // TR: Geri seçeneği
    secim = input("Select an option (Bir seçenek seçin): ")  # EN: Get menu selection // TR: Menü seçimini al
    if secim == '1':
        musteri_alisveris_menu(kullanici_adi)  # EN: Go to shopping menu // TR: Alışveriş menüsüne git
    elif secim == '2':
        musteri_kupon_goruntule(kullanici_adi)  # EN: Show coupons // TR: Kuponları göster
    elif secim == '3':
        musteri_minigame_menu(kullanici_adi)  # EN: Go to minigame menu // TR: Mini oyun menüsüne git
    elif secim == '4':
        musteri_bakiye_yukle(kullanici_adi)  # EN: Go to add balance // TR: Bakiye yükleme menüsüne git
    elif secim == '5':
        musteri_alisveris_gecmisi(kullanici_adi)  # EN: Show purchase history // TR: Alışveriş geçmişini göster
    elif secim == '6':
        musteri_minigame_scoreboard()  # EN: Show minigame scoreboard // TR: Mini oyun skor tablosunu göster
    else:
        ana_menu()  # EN: Go back to main menu // TR: Ana menüye dön

# Customer coupon view
# Müşteri kuponlarını görüntüleme fonksiyonu
def musteri_kupon_goruntule(kullanici_adi):  # EN: Show customer's coupons // TR: Müşterinin kuponlarını göster
    print("\n--- Your Coupons / Kuponlarınız ---")  # EN: Print coupon title // TR: Kupon başlığını yazdır
    bulundu = False  # EN: Flag for coupon found // TR: Kupon bulundu bayrağı
    with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:  # EN: Open coupons file // TR: Kuponlar dosyasını aç
        kuponlar = f.readlines()  # EN: Read all coupons // TR: Tüm kuponları oku
    for satir in kuponlar:  # EN: Loop through coupons // TR: Kuponları döngüyle gez
        parcalar = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(parcalar) > 1 and parcalar[0] == kullanici_adi:  # EN: If coupon belongs to user // TR: Kupon kullanıcıya aitse
            print(f"Coupon: %{parcalar[1]} discount / Kupon: %{parcalar[1]} indirim")  # EN: Print coupon info // TR: Kupon bilgisini yazdır
            bulundu = True  # EN: Set found flag // TR: Bayrağı true yap
    if not bulundu:  # EN: If no coupon found // TR: Kupon yoksa
        print("No coupons found! / Kuponunuz yok!")  # EN: Print no coupon message // TR: Kupon yok mesajı
    musteri_menu(kullanici_adi)  # EN: Return to customer menu // TR: Müşteri menüsüne dön

# Shopping menu for customer
# Müşteri için alışveriş menüsü
def musteri_alisveris_menu(kullanici_adi):  # EN: Customer shopping menu // TR: Müşteri alışveriş menüsü
    urunler = {  # EN: Product dictionary // TR: Ürün sözlüğü
        '1001': ['Muz', 15],  # EN: Banana // TR: Muz
        '1002': ['Elma', 10],  # EN: Apple // TR: Elma
        '1003': ['Domates', 8],  # EN: Tomato // TR: Domates
        '1004': ['Salatalık', 7],  # EN: Cucumber // TR: Salatalık
        '1005': ['Portakal', 12]  # EN: Orange // TR: Portakal
    }
    print("\n--- Shopping Menu / Alışveriş Menüsü ---")  # EN: Print shopping menu title // TR: Alışveriş menüsü başlığını yazdır
    print("Product List / Ürün Listesi:")  # EN: Print product list title // TR: Ürün listesi başlığını yazdır
    for kod, bilgi in urunler.items():  # EN: Loop through products // TR: Ürünleri döngüyle gez
        print(f"{kod} - {bilgi[0]}: {bilgi[1]} TL")  # EN: Print product info // TR: Ürün bilgisini yazdır
    urun_kodu = input("Enter product code or name (Ürün kodu veya adı girin): ")  # EN: Get product code or name // TR: Ürün kodu veya adı al
    secili_urun = None  # EN: Selected product // TR: Seçili ürün
    for kod, bilgi in urunler.items():  # EN: Loop to find selected product // TR: Seçili ürünü bulmak için döngü
        if urun_kodu == kod or urun_kodu.lower() == bilgi[0].lower():  # EN: If code or name matches // TR: Kod veya isim eşleşirse
            secili_urun = (kod, bilgi[0], bilgi[1])  # EN: Set selected product // TR: Seçili ürünü ayarla
    if secili_urun is None:  # EN: If product not found // TR: Ürün bulunamazsa
        print("Product not found! / Ürün bulunamadı!")  # EN: Print not found message // TR: Ürün bulunamadı mesajı
        musteri_alisveris_menu(kullanici_adi)  # EN: Return to shopping menu // TR: Alışveriş menüsüne dön
        return  # EN: Exit function // TR: Fonksiyondan çık
    # Stok kontrolü / Stock control
    stok_var = False  # EN: Stock available flag // TR: Stok var mı bayrağı
    stok_miktari = 0  # EN: Stock amount // TR: Stok miktarı
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:  # EN: Open stock file // TR: Stok dosyasını aç
        stoklar = f.readlines()  # EN: Read all stock lines // TR: Tüm stok satırlarını oku
    for satir in stoklar:  # EN: Loop through stock lines // TR: Stok satırlarını döngüyle gez
        parcalar = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(parcalar) > 2 and parcalar[0] == secili_urun[0]:  # EN: If product code matches // TR: Ürün kodu eşleşirse
            stok_miktari = int(parcalar[2])  # EN: Get stock amount // TR: Stok miktarını al
            if stok_miktari > 0:  # EN: If stock is positive // TR: Stok pozitifse
                stok_var = True  # EN: Set stock available // TR: Stok var bayrağını true yap
    if not stok_var or stok_miktari == 0:  # EN: If no stock // TR: Stok yoksa
        print("This product is out of stock! / Bu ürün stokta yok!")  # EN: Print out of stock message // TR: Stokta yok mesajı
        musteri_menu(kullanici_adi)  # EN: Return to customer menu // TR: Müşteri menüsüne dön
        return  # EN: Exit function // TR: Fonksiyondan çık
    adet = input(f"How many {secili_urun[1]}? (Kaç adet {secili_urun[1]}?): ")  # EN: Get quantity // TR: Adet al
    if not adet.isdigit() or int(adet) < 1:  # EN: If invalid quantity // TR: Geçersiz adet ise
        print("Invalid quantity! / Geçersiz adet!")  # EN: Print invalid quantity message // TR: Geçersiz adet mesajı
        musteri_alisveris_menu(kullanici_adi)  # EN: Return to shopping menu // TR: Alışveriş menüsüne dön
        return  # EN: Exit function // TR: Fonksiyondan çık
    adet = int(adet)  # EN: Convert quantity to int // TR: Adeti tam sayıya çevir
    if adet > stok_miktari:  # EN: If not enough stock // TR: Yeterli stok yoksa
        print(f"Not enough stock! Only {stok_miktari} left. / Yeterli stok yok! Sadece {stok_miktari} adet kaldı.")  # EN: Print not enough stock // TR: Yeterli stok yok mesajı
        musteri_alisveris_menu(kullanici_adi)  # EN: Return to shopping menu // TR: Alışveriş menüsüne dön
        return  # EN: Exit function // TR: Fonksiyondan çık
    toplam_tutar = adet * secili_urun[2]  # EN: Calculate total price // TR: Toplam fiyatı hesapla
    # Kupon kontrolü / Check for coupon
    kupon_var = False  # EN: Coupon available flag // TR: Kupon var mı bayrağı
    kupon_orani = 0  # EN: Coupon discount percent // TR: Kupon indirim oranı
    with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:  # EN: Open coupons file // TR: Kuponlar dosyasını aç
        kuponlar = f.readlines()  # EN: Read all coupons // TR: Tüm kuponları oku
    for satir in kuponlar:  # EN: Loop through coupons // TR: Kuponları döngüyle gez
        parcalar = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(parcalar) > 1 and parcalar[0] == kullanici_adi:  # EN: If coupon belongs to user // TR: Kupon kullanıcıya aitse
            kupon_var = True  # EN: Set coupon available // TR: Kupon var bayrağını true yap
            kupon_orani = int(parcalar[1])  # EN: Get coupon percent // TR: Kupon oranını al
    if kupon_var:  # EN: If coupon is available // TR: Kupon varsa
        print(f"You have a coupon: %{kupon_orani} discount! / Kuponunuz var: %{kupon_orani} indirim!")  # EN: Show coupon info // TR: Kupon bilgisini göster
        kullan = input("Use coupon? (y/n) / Kupon kullanılsın mı? (e/h): ")  # EN: Ask to use coupon // TR: Kupon kullanılsın mı sor
        if kullan.lower() == 'y' or kullan.lower() == 'e':  # EN: If user wants to use coupon // TR: Kullanıcı kuponu kullanmak isterse
            indirim = toplam_tutar * kupon_orani // 100  # EN: Calculate discount // TR: İndirimi hesapla
            toplam_tutar -= indirim  # EN: Apply discount // TR: İndirimi uygula
            print(f"Discounted total: {toplam_tutar} TL / İndirimli toplam: {toplam_tutar} TL")  # EN: Show discounted total // TR: İndirimli toplamı göster
            # Kuponu sil / Remove coupon after use  # EN: Remove coupon after use // TR: Kuponu kullandıktan sonra sil
            yeni_kuponlar = []  # EN: New coupon list // TR: Yeni kupon listesi
            for satir in kuponlar:  # EN: Loop through coupons // TR: Kuponları döngüyle gez
                if not (satir.startswith(kullanici_adi + ',')):  # EN: If not this user's coupon // TR: Bu kullanıcıya ait değilse
                    yeni_kuponlar.append(satir)  # EN: Keep coupon // TR: Kuponu sakla
            with open(dosya_dict['coupons'], 'w', encoding='utf-8') as f:  # EN: Open coupon file to write // TR: Kupon dosyasını yazmak için aç
                for satir in yeni_kuponlar:  # EN: Write remaining coupons // TR: Kalan kuponları yaz
                    f.write(satir)  # EN: Write coupon // TR: Kuponu yaz

    # Müşteri bakiyesini oku / Read customer balance  # EN: Read customer balance // TR: Müşteri bakiyesini oku
    with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:  # EN: Open customer file // TR: Müşteri dosyasını aç
        musteriler = f.readlines()  # EN: Read all customers // TR: Tüm müşterileri oku
    yeni_musteriler = []  # EN: New customer list // TR: Yeni müşteri listesi
    bakiye = 0  # EN: Customer balance // TR: Müşteri bakiyesi
    for satir in musteriler:  # EN: Loop through customers // TR: Müşterileri döngüyle gez
        bilgiler = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(bilgiler) > 4 and bilgiler[2] == kullanici_adi:  # EN: If this is the user // TR: Bu kullanıcı ise
            bakiye = int(bilgiler[4])  # EN: Get balance // TR: Bakiyeyi al
    if bakiye < toplam_tutar:  # EN: If not enough balance // TR: Yeterli bakiye yoksa
        print(f"Insufficient balance! / Yetersiz bakiye! (Balance/Bakiye: {bakiye} TL)")  # EN: Show insufficient balance // TR: Yetersiz bakiye göster
        musteri_menu(kullanici_adi)  # EN: Return to customer menu // TR: Müşteri menüsüne dön
        return  # EN: Exit function // TR: Fonksiyondan çık

    # Bakiyeden düş / Deduct from balance  # EN: Deduct from balance // TR: Bakiyeden düş
    for satir in musteriler:  # EN: Loop through customers // TR: Müşterileri döngüyle gez
        bilgiler = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(bilgiler) > 4 and bilgiler[2] == kullanici_adi:  # EN: If this is the user // TR: Bu kullanıcı ise
            yeni_bakiye = bakiye - toplam_tutar  # EN: Calculate new balance // TR: Yeni bakiyeyi hesapla
            bilgiler[4] = str(yeni_bakiye)  # EN: Update balance // TR: Bakiyeyi güncelle
            yeni_musteriler.append(','.join(bilgiler) + '\n')  # EN: Add updated user // TR: Güncellenmiş kullanıcıyı ekle
        else:  # EN: If not this user // TR: Bu kullanıcı değilse
            yeni_musteriler.append(satir)  # EN: Keep as is // TR: Olduğu gibi ekle
    with open(dosya_dict['customer'], 'w', encoding='utf-8') as f:  # EN: Open customer file to write // TR: Müşteri dosyasını yazmak için aç
        for satir in yeni_musteriler:  # EN: Write all customers // TR: Tüm müşterileri yaz
            f.write(satir)  # EN: Write line // TR: Satırı yaz

    # Stoktan düş / Decrease stock  # EN: Decrease stock // TR: Stoktan düş
    yeni_stoklar = []  # EN: New stock list // TR: Yeni stok listesi
    for satir in stoklar:  # EN: Loop through stock // TR: Stokları döngüyle gez
        parcalar = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
        if len(parcalar) > 2 and parcalar[0] == secili_urun[0]:  # EN: If this is the product // TR: Bu ürün ise
            yeni_stok = stok_miktari - adet  # EN: Calculate new stock // TR: Yeni stok miktarını hesapla
            yeni_stoklar.append(parcalar[0] + ',' + parcalar[1] + ',' + str(yeni_stok) + '\n')  # EN: Update stock // TR: Stok bilgisini güncelle
        else:  # EN: If not this product // TR: Bu ürün değilse
            yeni_stoklar.append(satir)  # EN: Keep as is // TR: Olduğu gibi ekle
    with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:  # EN: Open stock file to write // TR: Stok dosyasını yazmak için aç
        for satir in yeni_stoklar:  # EN: Write all stock // TR: Tüm stokları yaz
            f.write(satir)  # EN: Write line // TR: Satırı yaz

    # Alışverişi kaydet / Save purchase  # EN: Save purchase // TR: Alışverişi kaydet
    with open(dosya_dict['purchases'], 'a', encoding='utf-8') as f:  # EN: Open purchases file to append // TR: Alışveriş dosyasını ekleme için aç
        f.write(kullanici_adi + ',' + secili_urun[0] + ',' + secili_urun[1] + ',' + str(adet) + ',' + str(toplam_tutar) + '\n')  # EN: Write purchase info // TR: Alışveriş bilgisini yaz

    print(f"Purchase completed and saved! / Alışveriş tamamlandı ve kaydedildi! New balance/Yeni bakiye: {yeni_bakiye} TL")  # EN: Show success message // TR: Başarı mesajı göster
    musteri_menu(kullanici_adi)  # EN: Return to customer menu // TR: Müşteri menüsüne dön

# Add balance to customer account
# Müşteri bakiyesine para ekleme fonksiyonu
def musteri_bakiye_yukle(kullanici_adi):
    print("\n--- Add Balance / Bakiye Yükle ---")
    miktar = input("Enter amount to add (Eklenecek miktarı girin): ")
    if not miktar.isdigit() or int(miktar) < 1:
        print("Invalid amount! / Geçersiz miktar!")
        musteri_bakiye_yukle(kullanici_adi)
        return
    miktar = int(miktar)
    # Read customers / Müşterileri oku
    with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
        musteriler = f.readlines()
    yeni_musteriler = []
    for satir in musteriler:
        bilgiler = satir.strip().split(',')
        if len(bilgiler) > 4 and bilgiler[2] == kullanici_adi:
            eski_bakiye = int(bilgiler[4])
            yeni_bakiye = eski_bakiye + miktar
            bilgiler[4] = str(yeni_bakiye)
            yeni_musteriler.append(','.join(bilgiler) + '\n')
        else:
            yeni_musteriler.append(satir)
    with open(dosya_dict['customer'], 'w', encoding='utf-8') as f:
        for satir in yeni_musteriler:
            f.write(satir)
    print(f"Balance added! New balance: {yeni_bakiye} TL / Bakiye yüklendi! Yeni bakiye: {yeni_bakiye} TL")
    musteri_menu(kullanici_adi)

# Customer purchase history
# Müşteri alışveriş geçmişi fonksiyonu
def musteri_alisveris_gecmisi(kullanici_adi):
    print("\n--- Purchase History / Alışveriş Geçmişi ---")
    bulundu = False
    with open(dosya_dict['purchases'], 'r', encoding='utf-8') as f:
        kayitlar = f.readlines()
    for satir in kayitlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 4 and parcalar[0] == kullanici_adi:
            print(f"Product: {parcalar[2]}, Quantity: {parcalar[3]}, Total: {parcalar[4]} TL / Ürün: {parcalar[2]}, Adet: {parcalar[3]}, Toplam: {parcalar[4]} TL")
            bulundu = True
    if not bulundu:
        print("No purchases found! / Alışveriş kaydınız yok!")
    musteri_menu(kullanici_adi)

# Minigame menu
# Mini oyun menüsü
def musteri_minigame_menu(kullanici_adi):
    print("\n--- Minigame Menu / Mini Oyun Menüsü ---")
    print("1. Play Game (Oyun Oyna)")
    print("2. View Scoreboard (Skor Tablosu)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        musteri_minigame_oyna(kullanici_adi)
    elif secim == '2':
        musteri_minigame_scoreboard()
    else:
        musteri_menu(kullanici_adi)

# Minigame: Market Taş-Kağıt-Makas
# Mini oyun: Market Rock-Paper-Scissors
def musteri_minigame_oyna(kullanici_adi):
    import random
    import datetime
    print("\n--- Market Minigame / Market Mini Oyun ---")
    secenekler = ['Elma', 'Muz', 'Portakal']  # Apple, Banana, Orange
    print("Choose one: 1-Elma (Apple), 2-Muz (Banana), 3-Portakal (Orange)")
    oyuncu_secim = input("Your choice (Seçiminiz): ")
    if oyuncu_secim not in ['1', '2', '3']:
        print("Invalid choice! / Geçersiz seçim!")
        musteri_minigame_oyna(kullanici_adi)
        return
    oyuncu = secenekler[int(oyuncu_secim)-1]
    bilgisayar = random.choice(secenekler)
    print(f"Computer chose: {bilgisayar} / Bilgisayarın seçimi: {bilgisayar}")
    # Oyun kuralları: Elma > Muz, Muz > Portakal, Portakal > Elma
    kazanma = {'Elma': 'Muz', 'Muz': 'Portakal', 'Portakal': 'Elma'}
    if oyuncu == bilgisayar:
        print("Draw! / Berabere!")
        skor_guncelle(kullanici_adi, 0)
    elif kazanma[oyuncu] == bilgisayar:
        print("You win! / Kazandınız!")
        skor_guncelle(kullanici_adi, 1)
        # Son 2 haftada kupon aldı mı kontrol et ve kupon ver
        if not son_iki_haftada_kupon_var_mi(kullanici_adi):
            kupon_oran = random.choice([5, 10, 15])  # Dinamik oran
            with open(dosya_dict['coupons'], 'a', encoding='utf-8') as f:
                f.write(kullanici_adi + ',' + str(kupon_oran) + '\n')
            print(f"You won a coupon! %{kupon_oran} discount / Kupon kazandınız! %{kupon_oran} indirim")
    else:
        print("You lose! / Kaybettiniz!")
        skor_guncelle(kullanici_adi, -1)
    musteri_minigame_menu(kullanici_adi)

# Skor güncelleme fonksiyonu
# Update scoreboard function
def skor_guncelle(kullanici_adi, sonuc):
    import datetime
    # Skor dosyasını oku / Read scoreboard
    try:
        with open(dosya_dict['scoreboard'], 'r', encoding='utf-8') as f:
            skorlar = f.readlines()
    except:
        skorlar = []
    yeni_skorlar = []
    bulundu = False
    for satir in skorlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2 and parcalar[0] == kullanici_adi:
            skor = int(parcalar[1]) + sonuc
            tarih = datetime.datetime.now().strftime('%Y-%m-%d')
            yeni_skorlar.append(kullanici_adi + ',' + str(skor) + ',' + tarih + '\n')
            bulundu = True
        else:
            yeni_skorlar.append(satir)
    if not bulundu:
        tarih = datetime.datetime.now().strftime('%Y-%m-%d')
        yeni_skorlar.append(kullanici_adi + ',' + str(sonuc) + ',' + tarih + '\n')
    with open(dosya_dict['scoreboard'], 'w', encoding='utf-8') as f:
        for satir in yeni_skorlar:
            f.write(satir)

# Skor tablosunu göster
# Show scoreboard
def musteri_minigame_scoreboard():
    print("\n--- Minigame Scoreboard / Mini Oyun Skor Tablosu ---")
    try:
        with open(dosya_dict['scoreboard'], 'r', encoding='utf-8') as f:
            skorlar = f.readlines()
    except:
        skorlar = []
    if not skorlar:
        print("No scores yet! / Henüz skor yok!")
        return
    for satir in skorlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            print(f"User: {parcalar[0]}, Score: {parcalar[1]}, Last Game: {parcalar[2]} / Kullanıcı: {parcalar[0]}, Skor: {parcalar[1]}, Son Oyun: {parcalar[2]}")

# Son 2 haftada kupon aldı mı kontrol et
# Check if user got a coupon in last 2 weeks
def son_iki_haftada_kupon_var_mi(kullanici_adi):
    import datetime
    try:
        with open(dosya_dict['scoreboard'], 'r', encoding='utf-8') as f:
            skorlar = f.readlines()
    except:
        return False
    for satir in skorlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2 and parcalar[0] == kullanici_adi:
            tarih = parcalar[2]
            try:
                oyun_tarihi = datetime.datetime.strptime(tarih, '%Y-%m-%d')
                bugun = datetime.datetime.now()
                fark = (bugun - oyun_tarihi).days
                if fark < 14:
                    return True
            except:
                continue
    return False

# Admin login menu
# Admin giriş menüsü
def admin_giris_menu():
    print("\n--- Admin Login / Admin Girişi ---")
    admin_adi = input("Admin Name (Admin Adı): ")
    sifre = input("Password (Şifre): ")
    with open(dosya_dict['admin'], 'r', encoding='utf-8') as f:
        satirlar = f.readlines()
    giris_basarili = False
    for satir in satirlar:
        bilgiler = satir.strip().split(',')
        if len(bilgiler) > 1 and bilgiler[0] == admin_adi and bilgiler[1] == sifre:
            giris_basarili = True
    if giris_basarili:
        print("Admin login successful! / Admin girişi başarılı!")
        admin_menu(admin_adi)
    else:
        print("Wrong admin name or password! / Hatalı admin adı veya şifre!")
        ana_menu()

# Admin menu (to be developed)
# Admin menüsü (geliştirilecek)
def admin_menu(admin_adi):
    print(f"\n--- Admin Menu for {admin_adi} / {admin_adi} için Admin Menüsü ---")
    print("1. Inspection (Denetim)")
    print("2. Customer List (Müşteri Listesi)")
    print("3. Most Purchased (En Çok Alınanlar)")
    print("4. Storage (Depo)")
    print("5. Wholesaler Search (Toptancı Arama)")
    print("6. View/Update Stock (Stokları Görüntüle/Güncelle)")
    print("7. Order from Wholesaler (Toptancıdan Sipariş Ver)")
    print("8. Add Coupon to Customer (Müşteriye Kupon Tanımla)")
    print("9. Sales Statistics (Satış İstatistikleri)")
    print("10. Warehouse Layout (Depo Yerleşimi)")
    print("11. Shortest Path in Warehouse (Depoda Kısa Yol)")
    print("12. Expiry/Decay Tracking (Çürüme/SKT Takibi)")
    print("13. Audit & Theft Control (Denetim ve Hırsızlık Kontrolü)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '6':
        admin_stok_goruntule_guncelle()
    elif secim == '7':
        admin_toptanci_siparis()
    elif secim == '8':
        admin_kupon_tanimla()
    elif secim == '9':
        admin_satis_istatistik()
    elif secim == '10':
        admin_depo_yerlesim()
    elif secim == '11':
        admin_depo_kisayol()
    elif secim == '12':
        admin_urun_curume_takip()
    elif secim == '13':
        admin_denetim_hirsizlik()
    else:
        ana_menu()

# Admin stock view and update
# Admin stok görüntüleme ve güncelleme fonksiyonu
def admin_stok_goruntule_guncelle():
    print("\n--- Stock List / Stok Listesi ---")
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            print(f"Code: {parcalar[0]}, Name: {parcalar[1]}, Stock: {parcalar[2]} / Kod: {parcalar[0]}, Ad: {parcalar[1]}, Stok: {parcalar[2]}")
    print("1. Update Stock (Stok Güncelle)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        urun_kodu = input("Enter product code to update (Güncellenecek ürün kodunu girin): ")
        yeni_stok = input("Enter new stock amount (Yeni stok miktarını girin): ")
        if not yeni_stok.isdigit() or int(yeni_stok) < 0:  # EN: If new stock is not a digit or less than 0 // TR: Yeni stok bir sayı değilse veya 0'dan küçükse
            print("Invalid stock amount! / Geçersiz stok miktarı!")  # EN: Print invalid stock message // TR: Geçersiz stok mesajı yazdır
            admin_stok_goruntule_guncelle()  # EN: Call stock update menu again // TR: Stok güncelleme menüsünü tekrar çağır
            return  # EN: Exit function // TR: Fonksiyondan çık
        yeni_stok = int(yeni_stok)  # EN: Convert new stock to integer // TR: Yeni stok değerini tam sayıya çevir
        yeni_stoklar = []  # EN: New stock list // TR: Yeni stok listesi
        guncellendi = False  # EN: Update flag // TR: Güncellendi bayrağı
        for satir in stoklar:  # EN: Loop through stock lines // TR: Stok satırlarını döngüyle gez
            parcalar = satir.strip().split(',')  # EN: Split line by comma // TR: Satırı virgülle ayır
            if len(parcalar) > 2 and parcalar[0] == urun_kodu:  # EN: If product code matches // TR: Ürün kodu eşleşirse
                yeni_stoklar.append(parcalar[0] + ',' + parcalar[1] + ',' + str(yeni_stok) + '\n')  # EN: Update stock info // TR: Stok bilgisini güncelle
                guncellendi = True  # EN: Set update flag // TR: Güncellendi bayrağını true yap
            else:  # EN: If not this product // TR: Bu ürün değilse
                yeni_stoklar.append(satir)  # EN: Keep as is // TR: Olduğu gibi ekle
        if guncellendi:  # EN: If update happened // TR: Güncelleme olduysa
            with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:  # EN: Open stock file to write // TR: Stok dosyasını yazmak için aç
                for satir in yeni_stoklar:  # EN: Write all stock // TR: Tüm stokları yaz
                    f.write(satir)  # EN: Write line // TR: Satırı yaz
            print("Stock updated! / Stok güncellendi!")  # EN: Print stock updated message // TR: Stok güncellendi mesajı yazdır
        else:  # EN: If product code not found // TR: Ürün kodu bulunamadıysa
            print("Product code not found! / Ürün kodu bulunamadı!")  # EN: Print not found message // TR: Ürün kodu bulunamadı mesajı yazdır
        admin_stok_goruntule_guncelle()  # EN: Call stock update menu again // TR: Stok güncelleme menüsünü tekrar çağır
    else:
        admin_menu('admin')

# Admin wholesaler order function
# Admin toptancıdan sipariş verme fonksiyonu
def admin_toptanci_siparis():
    print("\n--- Wholesaler Order / Toptancıdan Sipariş ---")
    # Ürün fiyat listesi / Product price list
    urunler = {
        '1001': ['Muz', 15],
        '1002': ['Elma', 10],
        '1003': ['Domates', 8],
        '1004': ['Salatalık', 7],
        '1005': ['Portakal', 12]
    }
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    print("Current Stock / Mevcut Stok:")
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            print(f"{parcalar[0]} - {parcalar[1]}: {parcalar[2]}")
    urun_kodu = input("Enter product code to order (Sipariş verilecek ürün kodu): ")
    if urun_kodu not in urunler:
        print("Invalid product code! / Geçersiz ürün kodu!")
        admin_toptanci_siparis()
        return
    miktar = input("Enter quantity to order (Sipariş miktarı): ")
    if not miktar.isdigit() or int(miktar) < 1:
        print("Invalid quantity! / Geçersiz miktar!")
        admin_toptanci_siparis()
        return
    miktar = int(miktar)
    birim_fiyat = urunler[urun_kodu][1]
    toplam_fiyat = miktar * birim_fiyat
    # Admin bakiyesini oku / Read admin balance
    with open(dosya_dict['admin'], 'r', encoding='utf-8') as f:
        adminler = f.readlines()
    yeni_adminler = []
    bakiye = 0
    for satir in adminler:
        bilgiler = satir.strip().split(',')
        if len(bilgiler) > 2:
            bakiye = int(bilgiler[2])
    if bakiye < toplam_fiyat:
        print(f"Insufficient admin balance! / Yetersiz admin bakiyesi! (Balance/Bakiye: {bakiye} TL)")
        admin_menu('admin')
        return
    # Bakiyeden düş / Deduct from admin balance
    for satir in adminler:
        bilgiler = satir.strip().split(',')
        if len(bilgiler) > 2:
            yeni_bakiye = bakiye - toplam_fiyat
            bilgiler[2] = str(yeni_bakiye)
            yeni_adminler.append(','.join(bilgiler) + '\n')
        else:
            yeni_adminler.append(satir)
    with open(dosya_dict['admin'], 'w', encoding='utf-8') as f:
        for satir in yeni_adminler:
            f.write(satir)
    # Stok güncelle / Update stock
    yeni_stoklar = []
    stok_guncellendi = False
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2 and parcalar[0] == urun_kodu:
            yeni_stok = int(parcalar[2]) + miktar
            yeni_stoklar.append(parcalar[0] + ',' + parcalar[1] + ',' + str(yeni_stok) + '\n')
            stok_guncellendi = True
        else:
            yeni_stoklar.append(satir)
    if not stok_guncellendi:
        yeni_stoklar.append(urun_kodu + ',' + urunler[urun_kodu][0] + ',' + str(miktar) + '\n')
    with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:
        for satir in yeni_stoklar:
            f.write(satir)
    print(f"Order completed! {miktar} {urunler[urun_kodu][0]} added to stock. / Sipariş tamamlandı! {miktar} {urunler[urun_kodu][0]} stoğa eklendi.")
    print(f"Admin new balance: {yeni_bakiye} TL / Admin yeni bakiyesi: {yeni_bakiye} TL")
    admin_menu('admin')

# Admin coupon add function
# Admin müşteriye kupon tanımlama fonksiyonu
def admin_kupon_tanimla():
    print("\n--- Add Coupon to Customer / Müşteriye Kupon Tanımla ---")
    kullanici_adi = input("Enter customer username (Müşteri kullanıcı adını girin): ")
    oran = input("Enter discount percent (İndirim oranı girin, örn: 10): ")
    if not oran.isdigit() or int(oran) < 1 or int(oran) > 100:
        print("Invalid percent! / Geçersiz oran!")
        admin_kupon_tanimla()
        return
    oran = int(oran)
    # Kuponu ekle / Add coupon
    with open(dosya_dict['coupons'], 'a', encoding='utf-8') as f:
        f.write(kullanici_adi + ',' + str(oran) + '\n')
    print(f"Coupon added for {kullanici_adi}: %{oran} discount / {kullanici_adi} için kupon eklendi: %{oran} indirim")
    admin_menu('admin')

# Admin sales statistics
# Admin satış istatistikleri fonksiyonu
def admin_satis_istatistik():
    print("\n--- Sales Statistics / Satış İstatistikleri ---")
    urun_sayac = {}
    with open(dosya_dict['purchases'], 'r', encoding='utf-8') as f:
        kayitlar = f.readlines()
    for satir in kayitlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 4:
            urun = parcalar[2]
            adet = int(parcalar[3])
            if urun in urun_sayac:
                urun_sayac[urun] += adet
            else:
                urun_sayac[urun] = adet
    if not urun_sayac:
        print("No sales data found! / Satış verisi yok!")
        admin_menu('admin')
        return
    # Sırala ve yazdır / Sort and print
    sirali = sorted(urun_sayac.items(), key=lambda x: x[1], reverse=True)
    print("Most Purchased Products / En Çok Alınan Ürünler:")
    for urun, toplam in sirali:
        print(f"{urun}: {toplam} adet")
    admin_menu('admin')

# Warehouse layout function
# Depo yerleşimi fonksiyonu
def admin_depo_yerlesim():
    print("\n--- Warehouse Layout / Depo Yerleşimi ---")
    depo_boyut = 5  # 5x5 depo / 5x5 warehouse
    depo = [['-' for _ in range(depo_boyut)] for _ in range(depo_boyut)]
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 4:
            x = int(parcalar[3])
            y = int(parcalar[4])
            depo[x][y] = parcalar[1]  # Ürün adı / Product name
    print("Warehouse Map / Depo Haritası:")
    for i in range(depo_boyut):
        for j in range(depo_boyut):
            print(f"{depo[i][j]:10}", end=' ')
        print()
    admin_menu('admin')

# Shortest path in warehouse
# Depoda kısa yol fonksiyonu
def admin_depo_kisayol():
    print("\n--- Shortest Path in Warehouse / Depoda Kısa Yol ---")
    urun_kodu = input("Enter product code (Ürün kodu girin): ")
    hedef_x, hedef_y = -1, -1
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 4 and parcalar[0] == urun_kodu:
            hedef_x = int(parcalar[3])
            hedef_y = int(parcalar[4])
    if hedef_x == -1 or hedef_y == -1:
        print("Product not found or not placed! / Ürün bulunamadı veya yerleşmemiş!")
        admin_menu('admin')
        return
    # Depo giriş noktası (0,0) / Warehouse entrance (0,0)
    yol = []
    x, y = 0, 0
    while x != hedef_x or y != hedef_y:
        yol.append((x, y))
        if x < hedef_x:
            x += 1
        elif x > hedef_x:
            x -= 1
        elif y < hedef_y:
            y += 1
        elif y > hedef_y:
            y -= 1
    yol.append((hedef_x, hedef_y))
    print("Shortest path (Manhattan): / En kısa yol (Manhattan):")
    for adim in yol:
        print(f"Step: {adim} / Adım: {adim}")
    admin_menu('admin')

# Expiry/decay tracking function
# Çürüme/son kullanma tarihi takibi fonksiyonu
def admin_urun_curume_takip():
    import datetime
    print("\n--- Expiry/Decay Tracking / Çürüme/SKT Takibi ---")
    bugun = datetime.datetime.now().date()
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    uyarili_urunler = []
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 5:
            urun_adi = parcalar[1]
            miktar = parcalar[2]
            skt = parcalar[5]
            try:
                skt_tarih = datetime.datetime.strptime(skt, '%Y-%m-%d').date()
                kalan_gun = (skt_tarih - bugun).days
                if kalan_gun < 0:
                    print(f"EXPIRED: {urun_adi} ({miktar} adet) - Expired {abs(kalan_gun)} days ago! / SÜRESİ DOLMUŞ: {urun_adi} ({miktar} adet) - {abs(kalan_gun)} gün önce süresi doldu!")
                    uyarili_urunler.append((urun_adi, miktar, skt, kalan_gun))
                elif kalan_gun <= 5:
                    print(f"WARNING: {urun_adi} ({miktar} adet) - {kalan_gun} days left! / UYARI: {urun_adi} ({miktar} adet) - {kalan_gun} gün kaldı!")
                    uyarili_urunler.append((urun_adi, miktar, skt, kalan_gun))
            except:
                print(f"Invalid date for {urun_adi}! / {urun_adi} için geçersiz tarih!")
    if not uyarili_urunler:
        print("All products are fresh! / Tüm ürünler taze!")
    else:
        print("Suggestion: Renew these products soon! / Öneri: Bu ürünleri yakında yenileyin!")
    admin_menu('admin')

# Audit & theft control function
# Denetim ve hırsızlık kontrolü fonksiyonu
def admin_denetim_hirsizlik():
    import hashlib
    print("\n--- Audit & Theft Control / Denetim ve Hırsızlık Kontrolü ---")
    # Alınan ürünlerin hash kodları / Hash codes of purchased products
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    # Satılan ürünlerin toplamı / Total sold products
    satis_sayac = {}
    try:
        with open('sold_hashes.txt', 'r', encoding='utf-8') as f:
            satilan_hashlar = f.readlines()
    except:
        satilan_hashlar = []
    with open(dosya_dict['purchases'], 'r', encoding='utf-8') as f:
        alisverisler = f.readlines()
    for satir in alisverisler:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            kod = parcalar[1]
            adet = int(parcalar[3])
            if kod in satis_sayac:
                satis_sayac[kod] += adet
            else:
                satis_sayac[kod] = adet
    # Her ürün için kontrol / Check for each product
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            kod = parcalar[0]
            urun_adi = parcalar[1]
            stok_miktari = int(parcalar[2])
            # Alınan toplam miktar ve hash / Total purchased and hash
            alinmis = stok_miktari
            alinmis_hash = hashlib.md5((kod + str(alinmis)).encode()).hexdigest()
            # Satılan toplam miktar ve hash / Total sold and hash
            satilan = satis_sayac.get(kod, 0)
            satilan_hash = hashlib.md5((kod + str(satilan)).encode()).hexdigest()
            print(f"Product: {urun_adi} / Ürün: {urun_adi}")
            print(f"Stock hash: {alinmis_hash} | Sold hash: {satilan_hash}")
            # Eksik kontrolü / Missing check
            if alinmis < satilan:
                print(f"THEFT ALERT! Sold more than purchased! / HIRSIZLIK UYARISI! Satılandan fazla satış!")
            elif alinmis - satilan != stok_miktari:
                eksik = alinmis - satilan - stok_miktari
                print(f"MISSING: {eksik} units missing! / EKSİK: {eksik} adet kayıp!")
            else:
                print("No problem detected. / Sorun yok.")
    print("Audit complete. / Denetim tamamlandı.")
    admin_menu('admin')

# Programı başlat
# Start the program
ana_menu()
