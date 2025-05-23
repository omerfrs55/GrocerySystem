from cryptography.fernet import Fernet
import os
import time
import random
import datetime
#şifre leme için gerekli kütüphane
# Encryption key for Fernet  # EN: Encryption key for Fernet // TR: Fernet için şifreleme anahtarı
key = b'HQ8Q0Tf71laVCu-ACno2d34sBYYEqM34V5d-efdhyo4='
cipher = Fernet(key)
# Grocery System and Storage Main File  # Main file for the grocery system
# Market Sistemi ve Depolama Ana Dosyası  # Turkish title

# Files dictionary for .txt files  # EN: Dictionary for file paths // TR: Dosya yolları için sözlük
# .txt dosyaları için dosya sözlüğü  # EN: Turkish explanation // TR: Türkçe açıklama
dosya_dict = {
    'customer': 'customerRegister.txt',
    'admin': 'adminRegister.txt',
    'scoreboard': 'scoreboard.txt',
    'stock': 'stockproducts.txt',
    'coupons': 'coupons.txt',
    'purchases': 'customerPurchases.txt'
}

# Terminal temizleme fonksiyonu
def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# İşlem sonrası bekleme ve temizleme fonksiyonu
def islem_sonrasi_bekle():
    input("\nPress Enter to continue...")
    temizle()

# Main menu function  # EN: Main menu function // TR: Ana menü fonksiyonu
# Ana menü fonksiyonu  # EN: Turkish explanation // TR: Türkçe açıklama
def ana_menu():
    temizle()
    print("\n--- Grocery System and Storage ---")
    print("1. Customer Menu (Müşteri Menüsü)")
    print("2. Admin/Boss Menu (Yönetici/Patron Menüsü)")
    print("0. Exit (Çıkış)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        musteri_menu_secim()
    elif secim == '2':
        admin_giris_menu()
    elif secim == '0':
        print("Exiting... / Çıkılıyor...")
        islem_sonrasi_bekle()
        exit()
    else:
        print("Invalid selection! / Geçersiz seçim!")
        input("\nPress Enter to continue...")
        ana_menu()

def musteri_menu_secim():
    temizle()
    print("\n--- Customer Menu / Müşteri Menüsü ---")
    print("1. Login (Giriş Yap)")
    print("2. Register (Kayıt Ol)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        musteri_giris_menu()
    elif secim == '2':
        musteri_kayit()
    elif secim == '0':
        ana_menu()
    else:
        print("Invalid selection! / Geçersiz seçim!")
        input("\nPress Enter to continue...")
        musteri_menu_secim()

def musteri_kayit():
    temizle()
    print("\n--- Customer Registration / Müşteri Kaydı ---")
    ad = input("Name (Ad): ")
    soyad = input("Surname (Soyad): ")
    kullanici_adi = input("Username (Kullanıcı Adı): ")
    sifre = input("Password (Şifre): ")
    sifre_encoded = cipher.encrypt(sifre.encode()).decode()
    bakiye = '99999999'  # Yeni müşteriler 99999999 TL ile başlar
    
    try:
        with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
            satirlar = f.readlines()
        
        var_mi = False
        for satir in satirlar:
            bilgiler = satir.strip().split(',')
            if len(bilgiler) > 2 and bilgiler[2] == kullanici_adi:
                var_mi = True
                break
        
        if var_mi:
            print("This username is already taken! / Bu kullanıcı adı zaten alınmış!")
            input("\nPress Enter to continue...")
            musteri_menu_secim()
        else:
            with open(dosya_dict['customer'], 'a', encoding='utf-8') as f:
                f.write(f"{ad},{soyad},{kullanici_adi},{sifre_encoded},{bakiye}\n")
            print("Customer registered successfully! / Müşteri başarıyla kaydedildi!")
            input("\nPress Enter to continue...")
            musteri_menu_secim()
    except Exception as e:
        print(f"An error occurred! / Bir hata oluştu! Hata: {str(e)}")
        input("\nPress Enter to continue...")
        musteri_menu_secim()

# Customer login menu
# Müşteri giriş menüsü
def musteri_giris_menu():
    temizle()
    print("\n--- Customer Login / Müşteri Girişi ---")
    kullanici_adi = input("Username (Kullanıcı Adı): ")
    sifre = input("Password (Şifre): ")
    
    try:
        with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
            satirlar = f.readlines()
        
        giris_basarili = False
        for satir in satirlar:
            bilgiler = satir.strip().split(',')
            if len(bilgiler) > 3 and bilgiler[2] == kullanici_adi:
                try:
                    sifre_cozulmus = cipher.decrypt(bilgiler[3].encode()).decode()
                    if sifre == sifre_cozulmus:
                        giris_basarili = True
                        break
                except:
                    # Şifre şifrelenmemişse direkt karşılaştır
                    if sifre == bilgiler[3]:
                        giris_basarili = True
                        break

        if giris_basarili:
            print("Login successful! / Giriş başarılı!")
            islem_sonrasi_bekle()
            musteri_menu(kullanici_adi)
        else:
            print("Wrong username or password! / Hatalı kullanıcı adı veya şifre!")
            islem_sonrasi_bekle()
            ana_menu()
    except Exception as e:
        print(f"An error occurred! / Bir hata oluştu! Hata: {str(e)}")
        islem_sonrasi_bekle()
        ana_menu()

# Customer menu (to be developed)
# Müşteri menüsü (geliştirilecek)
def musteri_menu(kullanici_adi):
    temizle()
    print(f"\n--- Customer Menu for {kullanici_adi} / {kullanici_adi} için Müşteri Menüsü ---")
    print("1. Shopping (Alışveriş)")
    print("2. Coupons (Kuponlar)")
    print("3. Minigame (Mini Oyun)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        musteri_alisveris_menu(kullanici_adi)
    elif secim == '2':
        musteri_kupon_goruntule(kullanici_adi)
    elif secim == '3':
        musteri_minigame_menu(kullanici_adi)
    elif secim == '0':
        ana_menu()
    else:
        print("Invalid selection! / Geçersiz seçim!")
        input("\nPress Enter to continue...")
        musteri_menu(kullanici_adi)

# Customer coupon view
# Müşteri kuponlarını görüntüleme fonksiyonu
def musteri_kupon_goruntule(kullanici_adi):
    temizle()
    print("\n--- Your Coupons / Kuponlarınız ---")
    bulundu = False
    with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:
        kuponlar = f.readlines()
    for satir in kuponlar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 1 and parcalar[0] == kullanici_adi:
            print(f"Coupon: %{parcalar[1]} discount / Kupon: %{parcalar[1]} indirim")
            bulundu = True
    if not bulundu:
        print("No active coupons found! / Aktif kuponunuz bulunmamaktadır!")
    
    input("\nPress Enter to continue...")
    musteri_menu(kullanici_adi)

# Shopping menu for customer
# Müşteri için alışveriş menüsü
def musteri_alisveris_menu(kullanici_adi):
    temizle()
    print("\n--- Shopping Menu / Alışveriş Menüsü ---")
    sepet = {}  # Alışveriş sepeti
    
    # Ürün kategorileri
    meyveler = ['Elma', 'Muz', 'Portakal']
    sebzeler = ['Domates', 'Salatalık']
    
    # Kullanıcının alışveriş geçmişini oku
    kullanici_alisveris = {}
    try:
        with open(dosya_dict['purchases'], 'r', encoding='utf-8') as f:
            alisverisler = f.readlines()
        for satir in alisverisler:
            parcalar = satir.strip().split(',')
            if len(parcalar) > 2 and parcalar[0] == kullanici_adi:
                urun = parcalar[1]
                adet = int(parcalar[2])
                if urun in kullanici_alisveris:
                    kullanici_alisveris[urun] += adet
                else:
                    kullanici_alisveris[urun] = adet
    except:
        pass
    
    while True:
        print("\n" + "="*50)
        print("1. RAF - MEYVELER")
        print("="*50)
        
        # Meyveleri sırala
        siralanan_meyveler = []
        for meyve in meyveler:
            adet = kullanici_alisveris.get(meyve, 0)
            siralanan_meyveler.append((meyve, adet))
        siralanan_meyveler.sort(key=lambda x: x[1], reverse=True)
        
        # Meyveleri göster
        for i, (meyve, adet) in enumerate(siralanan_meyveler, 1):
            try:
                with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
                    stoklar = f.readlines()
                for satir in stoklar:
                    parcalar = satir.strip().split(',')
                    if len(parcalar) > 2 and parcalar[1].lower() == meyve.lower():
                        print(f"{i}. {meyve:<15} {parcalar[2]} TL (Stok: {parcalar[2]})")
                        break
            except:
                pass
        
        print("\n" + "="*50)
        print("2. RAF - SEBZELER")
        print("="*50)
        
        # Sebzeleri sırala
        siralanan_sebzeler = []
        for sebze in sebzeler:
            adet = kullanici_alisveris.get(sebze, 0)
            siralanan_sebzeler.append((sebze, adet))
        siralanan_sebzeler.sort(key=lambda x: x[1], reverse=True)
        
        # Sebzeleri göster
        for i, (sebze, adet) in enumerate(siralanan_sebzeler, 1):
            try:
                with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
                    stoklar = f.readlines()
                for satir in stoklar:
                    parcalar = satir.strip().split(',')
                    if len(parcalar) > 2 and parcalar[1].lower() == sebze.lower():
                        print(f"{i}. {sebze:<15} {parcalar[2]} TL (Stok: {parcalar[2]})")
                        break
            except:
                pass
        
        print("\n" + "="*50)
        print("1. Add to Cart (Sepete Ekle)")
        print("2. View Cart (Sepeti Görüntüle)")
        print("3. Complete Purchase (Alışverişi Tamamla)")
        print("0. Back (Geri)")
        
        secim = input("\nSelect an option (Bir seçenek seçin): ")
        
        if secim == '1':
            urun_kodu = input("Enter product name (Ürün adı girin): ")
            urun_bulundu = False
            
            # Tüm ürünleri birleştir
            tum_urunler = siralanan_meyveler + siralanan_sebzeler
            
            for urun, _ in tum_urunler:
                if urun.lower() == urun_kodu.lower():
                    try:
                        with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
                            stoklar = f.readlines()
                        for satir in stoklar:
                            parcalar = satir.strip().split(',')
                            if len(parcalar) > 2 and parcalar[1].lower() == urun.lower():
                                urun_bulundu = True
                                stok_miktari = int(parcalar[2])
                                adet = input(f"How many {urun}? (Kaç adet {urun}?): ")
                                if not adet.isdigit() or int(adet) < 1:
                                    print("Invalid quantity! / Geçersiz adet!")
                                    continue
                                adet = int(adet)
                                if adet > stok_miktari:
                                    print(f"Not enough stock! Only {stok_miktari} left. / Yeterli stok yok! Sadece {stok_miktari} adet kaldı.")
                                    continue
                                if urun in sepet:
                                    sepet[urun]['adet'] += adet
                                    sepet[urun]['toplam'] += adet * int(parcalar[2])
                                else:
                                    sepet[urun] = {
                                        'adet': adet,
                                        'fiyat': int(parcalar[2]),
                                        'toplam': adet * int(parcalar[2])
                                    }
                                print(f"{urun} added to cart! / {urun} sepete eklendi!")
                                break
                    except:
                        pass
                    break
            
            if not urun_bulundu:
                print("Product not found! / Ürün bulunamadı!")
                
        elif secim == '2':
            if not sepet:
                print("Your cart is empty! / Sepetiniz boş!")
            else:
                print("\nYour Cart / Sepetiniz:")
                toplam = 0
                for urun, detay in sepet.items():
                    print(f"{urun}: {detay['adet']} adet x {detay['fiyat']} TL = {detay['toplam']} TL")
                    toplam += detay['toplam']
                print(f"\nTotal / Toplam: {toplam} TL")
                
        elif secim == '3':
            if not sepet:
                print("Your cart is empty! / Sepetiniz boş!")
                continue
                
            print("\nYour Cart / Sepetiniz:")
            toplam = 0
            for urun, detay in sepet.items():
                print(f"{urun}: {detay['adet']} adet x {detay['fiyat']} TL = {detay['toplam']} TL")
                toplam += detay['toplam']
            print(f"\nTotal / Toplam: {toplam} TL")
            
            onay = input("\nDo you want to complete the purchase? (y/n) / Alışverişi tamamlamak istiyor musunuz? (e/h): ")
            if onay.lower() in ['y', 'e']:
                # Kupon kontrolü
                kupon_var = False
                kupon_orani = 0
                try:
                    with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:
                        kuponlar = f.readlines()
                    for satir in kuponlar:
                        parcalar = satir.strip().split(',')
                        if len(parcalar) > 1 and parcalar[0] == kullanici_adi:
                            kupon_var = True
                            kupon_orani = int(parcalar[1])
                            break
                except:
                    pass
                
                if kupon_var:
                    kupon_kullan = input(f"You have a %{kupon_orani} discount coupon. Use it? (y/n) / %{kupon_orani} indirim kuponunuz var. Kullanmak ister misiniz? (e/h): ")
                    if kupon_kullan.lower() in ['y', 'e']:
                        indirim = toplam * kupon_orani // 100
                        toplam -= indirim
                        print(f"Discount applied! New total: {toplam} TL / İndirim uygulandı! Yeni toplam: {toplam} TL")
                        # Kuponu sil
                        yeni_kuponlar = []
                        for satir in kuponlar:
                            if not satir.startswith(kullanici_adi + ','):
                                yeni_kuponlar.append(satir)
                        with open(dosya_dict['coupons'], 'w', encoding='utf-8') as f:
                            for satir in yeni_kuponlar:
                                f.write(satir)
                
                # Bakiye kontrolü
                try:
                    with open(dosya_dict['customer'], 'r', encoding='utf-8') as f:
                        musteriler = f.readlines()
                    bakiye = 0
                    for satir in musteriler:
                        bilgiler = satir.strip().split(',')
                        if len(bilgiler) > 4 and bilgiler[2] == kullanici_adi:
                            bakiye = int(bilgiler[4])
                    
                    if bakiye < toplam:
                        print(f"Insufficient balance! / Yetersiz bakiye! (Balance/Bakiye: {bakiye} TL)")
                        continue
                    
                    # Bakiyeden düş
                    yeni_musteriler = []
                    for satir in musteriler:
                        bilgiler = satir.strip().split(',')
                        if len(bilgiler) > 4 and bilgiler[2] == kullanici_adi:
                            yeni_bakiye = bakiye - toplam
                            bilgiler[4] = str(yeni_bakiye)
                            yeni_musteriler.append(','.join(bilgiler) + '\n')
                        else:
                            yeni_musteriler.append(satir)
                    with open(dosya_dict['customer'], 'w', encoding='utf-8') as f:
                        for satir in yeni_musteriler:
                            f.write(satir)
                    
                    # Stoktan düş
                    yeni_stoklar = []
                    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
                        stoklar = f.readlines()
                    for satir in stoklar:
                        parcalar = satir.strip().split(',')
                        if len(parcalar) > 2:
                            urun_adi = parcalar[1]
                            if urun_adi in sepet:
                                yeni_stok = int(parcalar[2]) - sepet[urun_adi]['adet']
                                yeni_stoklar.append(f"{parcalar[0]},{parcalar[1]},{yeni_stok}\n")
                            else:
                                yeni_stoklar.append(satir)
                    with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:
                        for satir in yeni_stoklar:
                            f.write(satir)
                    
                    # Alışverişi kaydet
                    with open(dosya_dict['purchases'], 'a', encoding='utf-8') as f:
                        for urun, detay in sepet.items():
                            f.write(f"{kullanici_adi},{urun},{detay['adet']},{detay['toplam']}\n")
                    
                    print(f"Purchase completed! New balance: {yeni_bakiye} TL / Alışveriş tamamlandı! Yeni bakiye: {yeni_bakiye} TL")
                    input("\nPress Enter to continue...")
                    musteri_menu(kullanici_adi)
                    return
                except Exception as e:
                    print(f"An error occurred during purchase! / Alışveriş sırasında bir hata oluştu! Hata: {str(e)}")
                    continue
                
        elif secim == '0':
            musteri_menu(kullanici_adi)
            return
        else:
            print("Invalid selection! / Geçersiz seçim!")
        
        input("\nPress Enter to continue...")
        temizle()

# Minigame menu
# Mini oyun menüsü
def musteri_minigame_menu(kullanici_adi):
    temizle()
    print("\n--- Minigame Menu / Mini Oyun Menüsü ---")
    print("1. Play Game (Oyun Oyna)")
    print("2. View Scoreboard (Skor Tablosu)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        musteri_minigame_oyna(kullanici_adi)
    elif secim == '2':
        musteri_minigame_scoreboard(kullanici_adi)
    elif secim == '0':
        musteri_menu(kullanici_adi)
    else:
        print("Invalid selection! / Geçersiz seçim!")
        islem_sonrasi_bekle()
        musteri_minigame_menu(kullanici_adi)

# Minigame: Muz Elma Muz
# Mini oyun: Muz Elma Muz
def musteri_minigame_oyna(kullanici_adi):
    temizle()
    print("\n--- Muz Elma Muz Game / Muz Elma Muz Oyunu ---")
    
    # Son kupon kazanma tarihini kontrol et
    son_kupon_tarihi = None
    try:
        with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:
            kuponlar = f.readlines()
        for satir in kuponlar:
            parcalar = satir.strip().split(',')
            if len(parcalar) > 2 and parcalar[0] == kullanici_adi:
                son_kupon_tarihi = datetime.datetime.strptime(parcalar[2], '%Y-%m-%d')
    except:
        pass

    # Kupon kazanma kontrolü
    kupon_kazanabilir = True
    if son_kupon_tarihi:
        gecen_gun = (datetime.datetime.now() - son_kupon_tarihi).days
        if gecen_gun < 14:  # 2 hafta = 14 gün
            kupon_kazanabilir = False
            print(f"\nSon kuponunuzdan bu yana {gecen_gun} gün geçti. Yeni kupon için {14-gecen_gun} gün daha beklemelisiniz.")

    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = '🍎'  # Kullanıcı Elma, bilgisayar Muz
            self.winner = None
            self.game_over = False
        
        def print_board(self):
            print("\n")
            for i in range(3):
                print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")
                if i < 2:
                    print("-----------")
            print("\n")
        
        def make_move(self, row, col):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
            return False
        
        def check_winner(self):
            # Yatay kontrol
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                    self.winner = self.board[i][0]
                    return True
            
            # Dikey kontrol
            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                    self.winner = self.board[0][i]
                    return True
            
            # Çapraz kontrol
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                self.winner = self.board[0][0]
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                self.winner = self.board[0][2]
                return True
            
            # Beraberlik kontrolü
            if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
                self.winner = 'Draw'
                return True
            
            return False
        
        def minimax(self, depth, is_maximizing):
            if self.check_winner():
                if self.winner == '🍎':
                    return -1
                elif self.winner == '🍌':
                    return 1
                else:
                    return 0
            
            if is_maximizing:
                best_score = float('-inf')
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            self.board[i][j] = '🍌'
                            score = self.minimax(depth + 1, False)
                            self.board[i][j] = ' '
                            best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            self.board[i][j] = '🍎'
                            score = self.minimax(depth + 1, True)
                            self.board[i][j] = ' '
                            best_score = min(score, best_score)
                return best_score
        
        def get_best_move(self):
            best_score = float('-inf')
            best_move = None
            
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = '🍌'
                        score = self.minimax(0, False)
                        self.board[i][j] = ' '
                        
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            
            return best_move
    
    oyun = TicTacToe()
    kazanma_sayisi = 0
    
    # Mevcut skoru al
    try:
        with open(dosya_dict['scoreboard'], 'r', encoding='utf-8') as f:
            skorlar = f.readlines()
        for satir in skorlar:
            parcalar = satir.strip().split(',')
            if len(parcalar) > 1 and parcalar[0] == kullanici_adi:
                kazanma_sayisi = int(parcalar[1])
    except:
        kazanma_sayisi = 0
    
    while not oyun.game_over:
        oyun.print_board()
        
        if oyun.current_player == '🍎':
            print("Sıra sizde! (1-9 arası bir sayı girin)")
            try:
                move = int(input("Hamleniz: ")) - 1
                row = move // 3
                col = move % 3
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if oyun.make_move(row, col):
                        if oyun.check_winner():
                            oyun.game_over = True
                        else:
                            oyun.current_player = '🍌'
                    else:
                        print("Geçersiz hamle! Lütfen boş bir kare seçin.")
                else:
                    print("Geçersiz hamle! 1-9 arası bir sayı girin.")
            except ValueError:
                print("Geçersiz giriş! Lütfen 1-9 arası bir sayı girin.")
        else:
            print("Bilgisayar düşünüyor...")
            time.sleep(1)
            best_move = oyun.get_best_move()
            if best_move:
                row, col = best_move
                oyun.make_move(row, col)
                if oyun.check_winner():
                    oyun.game_over = True
                else:
                    oyun.current_player = '🍎'
    
    oyun.print_board()
    
    if oyun.winner == '🍎':
        print("Tebrikler! Kazandınız!")
        kazanma_sayisi += 1
        skor_guncelle(kullanici_adi, 1)
        
        # Kupon kontrolü ve ekleme
        if kupon_kazanabilir:
            # Kullanıcının toplam kupon sayısını kontrol et
            toplam_kupon = 0
            try:
                with open(dosya_dict['coupons'], 'r', encoding='utf-8') as f:
                    kuponlar = f.readlines()
                for satir in kuponlar:
                    if satir.startswith(kullanici_adi + ','):
                        toplam_kupon += 1
            except:
                pass

            # İndirim oranını belirle (azalan oran)
            if toplam_kupon == 0:
                kupon_oran = 50  # İlk kupon %50
            elif toplam_kupon == 1:
                kupon_oran = 35  # İkinci kupon %35
            elif toplam_kupon == 2:
                kupon_oran = 25  # Üçüncü kupon %25
            else:
                kupon_oran = 15  # Sonraki kuponlar %15

            # Kuponu kaydet
            bugun = datetime.datetime.now().strftime('%Y-%m-%d')
            with open(dosya_dict['coupons'], 'a', encoding='utf-8') as f:
                f.write(f"{kullanici_adi},{kupon_oran},{bugun}\n")
            print(f"\nTebrikler! %{kupon_oran} indirim kuponu kazandınız!")
        else:
            print("\nPuanınız bir arttı!")
    elif oyun.winner == '🍌':
        print("Bilgisayar kazandı!")
        kazanma_sayisi = 0  # Kaybedince kazanma sayısı sıfırlanır
        skor_guncelle(kullanici_adi, -1)
    else:
        print("Berabere!")
        skor_guncelle(kullanici_adi, 0)
    
    input("\nDevam etmek için Enter'a basın...")
    musteri_menu(kullanici_adi)

# Skor güncelleme fonksiyonu
def skor_guncelle(kullanici_adi, sonuc):
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
            yeni_skorlar.append(f"{kullanici_adi},{skor},{tarih}\n")
            bulundu = True
        else:
            yeni_skorlar.append(satir)
    
    if not bulundu:
        tarih = datetime.datetime.now().strftime('%Y-%m-%d')
        yeni_skorlar.append(f"{kullanici_adi},{sonuc},{tarih}\n")
    
    with open(dosya_dict['scoreboard'], 'w', encoding='utf-8') as f:
        for satir in yeni_skorlar:
            f.write(satir)

# Skor tablosunu göster
def musteri_minigame_scoreboard(kullanici_adi):
    temizle()
    print("\n--- Minigame Scoreboard / Mini Oyun Skor Tablosu ---")
    try:
        with open(dosya_dict['scoreboard'], 'r', encoding='utf-8') as f:
            skorlar = f.readlines()
        
        if not skorlar:
            print("No scores yet! / Henüz skor yok!")
        else:
            # Skorları büyükten küçüğe sırala
            skor_listesi = []
            for satir in skorlar:
                parcalar = satir.strip().split(',')
                if len(parcalar) > 2:
                    skor_listesi.append((parcalar[0], int(parcalar[1]), parcalar[2]))
            
            # Skorları büyükten küçüğe sırala
            skor_listesi.sort(key=lambda x: x[1], reverse=True)
            
            print("\nSıra  Kullanıcı Adı    Skor    Son Oyun")
            print("-" * 45)
            for i, (kullanici, skor, tarih) in enumerate(skor_listesi, 1):
                print(f"{i:<5} {kullanici:<15} {skor:<8} {tarih}")
    except Exception as e:
        print(f"An error occurred! / Bir hata oluştu! Hata: {str(e)}")
    
    input("\nPress Enter to continue...")
    musteri_minigame_menu(kullanici_adi)

# Admin login menu
# Admin giriş menüsü
def admin_giris_menu():
    temizle()
    print("\n--- Admin Login / Admin Girişi ---")
    admin_adi = input("Admin Name (Admin Adı): ")
    sifre = input("Password (Şifre): ")
    
    try:
        with open(dosya_dict['admin'], 'r', encoding='utf-8') as f:
            satirlar = f.readlines()
        
        giris_basarili = False
        for satir in satirlar:
            bilgiler = satir.strip().split(',')
            if len(bilgiler) >= 2:  # En az 2 bilgi olmalı (admin adı ve şifre)
                if bilgiler[0] == admin_adi and bilgiler[1] == sifre:
                    giris_basarili = True
                    break
        
        if giris_basarili:
            print("Admin login successful! / Admin girişi başarılı!")
            islem_sonrasi_bekle()
            admin_menu(admin_adi)
        else:
            print("Wrong admin name or password! / Hatalı admin adı veya şifre!")
            islem_sonrasi_bekle()
            ana_menu()
    except Exception as e:
        print(f"An error occurred! / Bir hata oluştu! Hata: {str(e)}")
        islem_sonrasi_bekle()
        ana_menu()

# Admin menu (to be developed)
# Admin menüsü (geliştirilecek)
def admin_menu(admin_adi):
    temizle()
    print(f"\n--- Admin Menu for {admin_adi} / {admin_adi} için Admin Menüsü ---")
    print("1. Most Purchased (En Çok Alınanlar)")
    print("2. View/Update Stock (Stokları Görüntüle/Güncelle)")
    print("3. Expiry/Decay Tracking (Çürüme/SKT Takibi)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        admin_en_cok_alinanlar()
    elif secim == '2':
        admin_stok_goruntule_guncelle()
    elif secim == '3':
        admin_urun_curume_takip()
    elif secim == '0':
        ana_menu()
    else:
        print("Invalid selection! / Geçersiz seçim!")
        input("\nPress Enter to continue...")
        admin_menu(admin_adi)

# Admin most purchased function
# Admin en çok alınanlar fonksiyonu
def admin_en_cok_alinanlar():
    temizle()
    print("\n--- Most Purchased Products / En Çok Alınan Ürünler ---")
    urun_sayac = {}
    with open(dosya_dict['purchases'], 'r', encoding='utf-8') as f:
        alisverisler = f.readlines()
    for satir in alisverisler:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 3:
            urun = parcalar[1]
            adet = int(parcalar[2])
            if urun in urun_sayac:
                urun_sayac[urun] += adet
            else:
                urun_sayac[urun] = adet
    
    # Majority vote ile sıralama
    sirali = sorted(urun_sayac.items(), key=lambda x: x[1], reverse=True)
    
    print("\nEn Çok Alınan Ürünler (Sıralı):")
    print("-" * 40)
    for i, (urun, adet) in enumerate(sirali, 1):
        print(f"{i}. {urun}: {adet} adet")
    
    # Bu sıralamayı stok dosyasına kaydet
    with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
        stoklar = f.readlines()
    
    yeni_stoklar = []
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            urun = parcalar[1]
            # Sıralama bilgisini ekle
            siralama = next((i for i, (u, _) in enumerate(sirali, 1) if u == urun), 0)
            if siralama > 0:
                parcalar.append(str(siralama))
            yeni_stoklar.append(','.join(parcalar) + '\n')
        else:
            yeni_stoklar.append(satir)
    
    with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:
        for satir in yeni_stoklar:
            f.write(satir)
    
    input("\nPress Enter to continue...")
    admin_menu('admin')

# Admin storage function
# depo fonksiyonu
def admin_stok_goruntule_guncelle():
    temizle()
    print("\n--- View/Update Stock / Stokları Görüntüle/Güncelle ---")
    print("1. View Stock (Stokları Görüntüle)")
    print("2. Update Stock (Stokları Güncelle)")
    print("0. Back (Geri)")
    secim = input("Select an option (Bir seçenek seçin): ")
    if secim == '1':
        print("\nCurrent Stock / Mevcut Stok:")
        with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
            stoklar = f.readlines()
        for satir in stoklar:
            parcalar = satir.strip().split(',')
            if len(parcalar) > 2:
                print(f"Product: {parcalar[1]}, Stock: {parcalar[2]} / Ürün: {parcalar[1]}, Stok: {parcalar[2]}")
    elif secim == '2':
        print("\nUpdate Stock / Stokları Güncelle:")
        urun = input("Enter product name (Ürün adı girin): ")
        miktar = input("Enter new stock quantity (Yeni stok miktarı girin): ")
        if not miktar.isdigit() or int(miktar) < 0:
            print("Invalid stock format! / Geçersiz stok formatı!")
            input("\nPress Enter to continue...")
            admin_menu('admin')
            return
        miktar = int(miktar)
        yeni_stoklar = []
        with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
            stoklar = f.readlines()
        for satir in stoklar:
            parcalar = satir.strip().split(',')
            if len(parcalar) > 2 and parcalar[1] == urun:
                parcalar[2] = str(miktar)
            yeni_stoklar.append(','.join(parcalar) + '\n')
        with open(dosya_dict['stock'], 'w', encoding='utf-8') as f:
            for satir in yeni_stoklar:
                f.write(satir)
        print(f"\nStock updated successfully! / Stok başarıyla güncellendi!")
    elif secim == '0':
        admin_menu('admin')
        return
    else:
        print("Invalid selection! / Geçersiz seçim!")
    input("\nPress Enter to continue...")
    admin_stok_goruntule_guncelle()

# Çürüme takibi fonksiyonu
def admin_urun_curume_takip():
    temizle()
    print("\n--- Expiry/Decay Tracking / Çürüme/SKT Takibi ---")
    
    try:
        with open(dosya_dict['stock'], 'r', encoding='utf-8') as f:
            stoklar = f.readlines()
    except:
        print("Stok verisi bulunamadı! / No stock data found!")
        islem_sonrasi_bekle()
        admin_menu('admin')
        return
    
    # Ürün çürüme süreleri (gün)
    curume_sureleri = {
        'Elma': 30,
        'Muz': 7,
        'Portakal': 14,
        'Domates': 5,
        'Salatalık': 7
    }
    
    bugun = datetime.datetime.now().date()
    uyarili_urunler = []
    
    print("\nÇürüme Takibi:")
    print("-" * 60)
    print(f"{'Ürün':<15} {'Miktar':<10} {'Çürüme Tarihi':<15} {'Kalan Gün':<10}")
    print("-" * 60)
    
    for satir in stoklar:
        parcalar = satir.strip().split(',')
        if len(parcalar) > 2:
            urun = parcalar[1]
            miktar = int(parcalar[2])
            
            if urun in curume_sureleri:
                curume_suresi = curume_sureleri[urun]
                curume_tarihi = bugun + datetime.timedelta(days=curume_suresi)
                kalan_gun = (curume_tarihi - bugun).days
                
                print(f"{urun:<15} {miktar:<10} {curume_tarihi.strftime('%Y-%m-%d'):<15} {kalan_gun:<10}")
                
                if kalan_gun <= 3:
                    uyarili_urunler.append((urun, miktar, curume_tarihi, kalan_gun))
    
    if uyarili_urunler:
        print("\nUYARI: Aşağıdaki ürünler yakında çürüyecek!")
        for urun, miktar, tarih, gun in uyarili_urunler:
            print(f"{urun}: {miktar} adet - {gun} gün kaldı!")
    else:
        print("\nTüm ürünler taze!")
    
    islem_sonrasi_bekle()
    admin_menu('admin')

# Programı başlat
# Start the program
ana_menu()
