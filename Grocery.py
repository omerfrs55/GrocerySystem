from cryptography.fernet import Fernet
import os
import time
import random
import datetime
#şifre leme için gerekli kütüphane
# Encryption key for Fernet  # EN: Encryption key for Fernet // TR: Fernet için şifreleme anahtarı
key = Fernet.generate_key() #SECRET_KEY='HQ8Q0Tf71laVCu-ACno2d34sBYYEqM34V5d-efdhyo4=' 
cipher = Fernet(key)
# Grocery System and Storage Main File  # Main file for the grocery system
# Market Sistemi ve Depolama Ana Dosyası  # Turkish title

# Files dictionary for .txt files  # EN: Dictionary for file paths // TR: Dosya yolları için sözlük
file_dict = {
    'customer': 'customerRegister.txt',
    'admin': 'adminRegister.txt',
    'scoreboard': 'scoreboard.txt',
    'stock': 'stockproducts.txt',
    'coupons': 'coupons.txt',
    'purchases': 'customerPurchases.txt'
}

# Terminal clearing function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Wait and clear function after operation
def wait_after_operation():
    input("\nPress Enter to continue...")
    clear()

# Main menu function
def main_menu():
    clear()
    print("\n--- Grocery System and Storage ---")
    print("1. Customer Menu")
    print("2. Admin/Boss Menu")
    print("0. Exit")
    choice = input("Select an option: ")
    if choice == '1':
        customer_menu_selection()
    elif choice == '2':
        admin_login_menu()
    elif choice == '0':
        print("Exiting...")
        wait_after_operation()
        exit()
    else:
        print("Invalid selection!")
        input("\nPress Enter to continue...")
        main_menu()

def customer_menu_selection():
    clear()
    print("\n--- Customer Menu ---")
    print("1. Login")
    print("2. Register")
    print("0. Back")
    choice = input("Select an option: ")
    if choice == '1':
        customer_login_menu()
    elif choice == '2':
        customer_register()
    elif choice == '0':
        main_menu()
    else:
        print("Invalid selection!")
        input("\nPress Enter to continue...")
        customer_menu_selection()

def customer_register():
    clear()
    print("\n--- Customer Registration ---")
    name = input("Name: ")
    surname = input("Surname: ")
    username = input("Username: ")
    password = input("Password: ")
    password_encoded = cipher.encrypt(password.encode()).decode()
    balance = '99999999'  # New customers start with 99999999 TL
    
    try:
        with open(file_dict['customer'], 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        exists = False
        for line in lines:
            info = line.strip().split(',')
            if len(info) > 2 and info[2] == username:
                exists = True
                break
        
        if exists:
            print("This username is already taken!")
            input("\nPress Enter to continue...")
            customer_menu_selection()
        else:
            with open(file_dict['customer'], 'a', encoding='utf-8') as f:
                f.write(f"{name},{surname},{username},{password_encoded},{balance}\n")
            print("Customer registered successfully!")
            input("\nPress Enter to continue...")
            customer_menu_selection()
    except Exception as e:
        print(f"An error occurred! Error: {str(e)}")
        input("\nPress Enter to continue...")
        customer_menu_selection()

def customer_login_menu():
    clear()
    print("\n--- Customer Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    try:
        with open(file_dict['customer'], 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        login_successful = False
        for line in lines:
            info = line.strip().split(',')
            if len(info) > 3 and info[2] == username:
                try:
                    decrypted_password = cipher.decrypt(info[3].encode()).decode()
                    if password == decrypted_password:
                        login_successful = True
                        break
                except:
                    if password == info[3]:
                        login_successful = True
                        break

        if login_successful:
            print("Login successful!")
            wait_after_operation()
            customer_menu(username)
        else:
            print("Wrong username or password!")
            wait_after_operation()
            main_menu()
    except Exception as e:
        print(f"An error occurred! Error: {str(e)}")
        wait_after_operation()
        main_menu()

def customer_menu(username):
    clear()
    print(f"\n--- Customer Menu for {username} ---")
    print("1. Shopping")
    print("2. Coupons")
    print("3. Minigame")
    print("0. Back")
    choice = input("Select an option: ")
    if choice == '1':
        customer_shopping_menu(username)
    elif choice == '2':
        customer_view_coupons(username)
    elif choice == '3':
        customer_minigame_menu(username)
    elif choice == '0':
        main_menu()
    else:
        print("Invalid selection!")
        input("\nPress Enter to continue...")
        customer_menu(username)

def customer_view_coupons(username):
    clear()
    print("\n--- Your Coupons ---")
    found = False
    with open(file_dict['coupons'], 'r', encoding='utf-8') as f:
        coupons = f.readlines()
    for line in coupons:
        parts = line.strip().split(',')
        if len(parts) > 1 and parts[0] == username:
            print(f"Coupon: %{parts[1]} discount")
            found = True
    if not found:
        print("No active coupons found!")
    
    input("\nPress Enter to continue...")
    customer_menu(username)

def customer_shopping_menu(username):
    clear()
    print("\n--- Shopping Menu ---")
    cart = {}  # Shopping cart
    
    # Product categories
    fruits = ['Apple', 'Banana', 'Orange']
    vegetables = ['Tomato', 'Cucumber']
    
    # Read user's shopping history
    user_purchases = {}
    try:
        with open(file_dict['purchases'], 'r', encoding='utf-8') as f:
            purchases = f.readlines()
        for line in purchases:
            parts = line.strip().split(',')
            if len(parts) > 2 and parts[0] == username:
                product = parts[1]
                quantity = int(parts[2])
                if product in user_purchases:
                    user_purchases[product] += quantity
                else:
                    user_purchases[product] = quantity
    except:
        pass
    
    while True:
        print("\n" + "="*50)
        print("1. SHELF - FRUITS")
        print("="*50)
        
        # Sort fruits
        sorted_fruits = []
        for fruit in fruits:
            quantity = user_purchases.get(fruit, 0)
            sorted_fruits.append((fruit, quantity))
        sorted_fruits.sort(key=lambda x: x[1], reverse=True)
        
        # Show fruits
        for i, (fruit, quantity) in enumerate(sorted_fruits, 1):
            try:
                with open(file_dict['stock'], 'r', encoding='utf-8') as f:
                    stocks = f.readlines()
                for line in stocks:
                    parts = line.strip().split(',')
                    if len(parts) > 2 and parts[1].lower() == fruit.lower():
                        print(f"{i}. {fruit:<15} {parts[2]} TL (Stock: {parts[2]})")
                        break
            except:
                pass
        
        print("\n" + "="*50)
        print("2. SHELF - VEGETABLES")
        print("="*50)
        
        # Sort vegetables
        sorted_vegetables = []
        for vegetable in vegetables:
            quantity = user_purchases.get(vegetable, 0)
            sorted_vegetables.append((vegetable, quantity))
        sorted_vegetables.sort(key=lambda x: x[1], reverse=True)
        
        # Show vegetables
        for i, (vegetable, quantity) in enumerate(sorted_vegetables, 1):
            try:
                with open(file_dict['stock'], 'r', encoding='utf-8') as f:
                    stocks = f.readlines()
                for line in stocks:
                    parts = line.strip().split(',')
                    if len(parts) > 2 and parts[1].lower() == vegetable.lower():
                        print(f"{i}. {vegetable:<15} {parts[2]} TL (Stock: {parts[2]})")
                        break
            except:
                pass
        
        print("\n" + "="*50)
        print("1. Add to Cart")
        print("2. View Cart")
        print("3. Complete Purchase")
        print("0. Back")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            product_code = input("Enter product name: ")
            product_found = False
            
            # Combine all products
            all_products = sorted_fruits + sorted_vegetables
            
            for product, _ in all_products:
                if product.lower() == product_code.lower():
                    try:
                        with open(file_dict['stock'], 'r', encoding='utf-8') as f:
                            stocks = f.readlines()
                        for line in stocks:
                            parts = line.strip().split(',')
                            if len(parts) > 2 and parts[1].lower() == product.lower():
                                product_found = True
                                stock_quantity = int(parts[2])
                                quantity = input(f"How many {product}?: ")
                                if not quantity.isdigit() or int(quantity) < 1:
                                    print("Invalid quantity!")
                                    continue
                                quantity = int(quantity)
                                if quantity > stock_quantity:
                                    print(f"Not enough stock! Only {stock_quantity} left.")
                                    continue
                                if product in cart:
                                    cart[product]['quantity'] += quantity
                                    cart[product]['total'] += quantity * int(parts[2])
                                else:
                                    cart[product] = {
                                        'quantity': quantity,
                                        'price': int(parts[2]),
                                        'total': quantity * int(parts[2])
                                    }
                                print(f"{product} added to cart!")
                                break
                    except:
                        pass
                    break
            
            if not product_found:
                print("Product not found!")
                
        elif choice == '2':
            if not cart:
                print("Your cart is empty!")
            else:
                print("\nYour Cart:")
                total = 0
                for product, details in cart.items():
                    print(f"{product}: {details['quantity']} x {details['price']} TL = {details['total']} TL")
                    total += details['total']
                print(f"\nTotal: {total} TL")
                
        elif choice == '3':
            if not cart:
                print("Your cart is empty!")
                continue
                
            print("\nYour Cart:")
            total = 0
            for product, details in cart.items():
                print(f"{product}: {details['quantity']} x {details['price']} TL = {details['total']} TL")
                total += details['total']
            print(f"\nTotal: {total} TL")
            
            confirm = input("\nDo you want to complete the purchase? (y/n): ")
            if confirm.lower() in ['y', 'e']:
                # Coupon check
                has_coupon = False
                coupon_rate = 0
                try:
                    with open(file_dict['coupons'], 'r', encoding='utf-8') as f:
                        coupons = f.readlines()
                    for line in coupons:
                        parts = line.strip().split(',')
                        if len(parts) > 1 and parts[0] == username:
                            has_coupon = True
                            coupon_rate = int(parts[1])
                            break
                except:
                    pass
                
                if has_coupon:
                    use_coupon = input(f"You have a %{coupon_rate} discount coupon. Use it? (y/n): ")
                    if use_coupon.lower() in ['y', 'e']:
                        discount = total * coupon_rate // 100
                        total -= discount
                        print(f"Discount applied! New total: {total} TL")
                        # Delete coupon
                        new_coupons = []
                        for line in coupons:
                            if not line.startswith(username + ','):
                                new_coupons.append(line)
                        with open(file_dict['coupons'], 'w', encoding='utf-8') as f:
                            for line in new_coupons:
                                f.write(line)
                
                # Balance check
                try:
                    with open(file_dict['customer'], 'r', encoding='utf-8') as f:
                        customers = f.readlines()
                    balance = 0
                    for line in customers:
                        info = line.strip().split(',')
                        if len(info) > 4 and info[2] == username:
                            balance = int(info[4])
                    
                    if balance < total:
                        print(f"Insufficient balance! (Balance: {balance} TL)")
                        continue
                    
                    # Deduct from balance
                    new_customers = []
                    for line in customers:
                        info = line.strip().split(',')
                        if len(info) > 4 and info[2] == username:
                            new_balance = balance - total
                            info[4] = str(new_balance)
                            new_customers.append(','.join(info) + '\n')
                        else:
                            new_customers.append(line)
                    with open(file_dict['customer'], 'w', encoding='utf-8') as f:
                        for line in new_customers:
                            f.write(line)
                    
                    # Deduct from stock
                    new_stocks = []
                    with open(file_dict['stock'], 'r', encoding='utf-8') as f:
                        stocks = f.readlines()
                    for line in stocks:
                        parts = line.strip().split(',')
                        if len(parts) > 2:
                            product_name = parts[1]
                            if product_name in cart:
                                new_stock = int(parts[2]) - cart[product_name]['quantity']
                                new_stocks.append(f"{parts[0]},{parts[1]},{new_stock}\n")
                            else:
                                new_stocks.append(line)
                    with open(file_dict['stock'], 'w', encoding='utf-8') as f:
                        for line in new_stocks:
                            f.write(line)
                    
                    # Save purchase
                    with open(file_dict['purchases'], 'a', encoding='utf-8') as f:
                        for product, details in cart.items():
                            f.write(f"{username},{product},{details['quantity']},{details['total']}\n")
                    
                    print(f"Purchase completed! New balance: {new_balance} TL")
                    input("\nPress Enter to continue...")
                    customer_menu(username)
                    return
                except Exception as e:
                    print(f"An error occurred during purchase! Error: {str(e)}")
                    continue
                
        elif choice == '0':
            customer_menu(username)
            return
        else:
            print("Invalid selection!")
        
        input("\nPress Enter to continue...")
        clear()

def customer_minigame_menu(username):
    clear()
    print("\n--- Minigame Menu ---")
    print("1. Play Game")
    print("2. View Scoreboard")
    print("0. Back")
    choice = input("Select an option: ")
    if choice == '1':
        customer_play_minigame(username)
    elif choice == '2':
        customer_minigame_scoreboard(username)
    elif choice == '0':
        customer_menu(username)
    else:
        print("Invalid selection!")
        wait_after_operation()
        customer_minigame_menu(username)

def customer_play_minigame(username):
    clear()
    print("\n--- Apple Banana Apple Game ---")
    
    # Check last coupon win date
    last_coupon_date = None
    try:
        with open(file_dict['coupons'], 'r', encoding='utf-8') as f:
            coupons = f.readlines()
        for line in coupons:
            parts = line.strip().split(',')
            if len(parts) > 2 and parts[0] == username:
                try:
                    last_coupon_date = datetime.datetime.strptime(parts[2], '%Y-%m-%d')
                except Exception as e:
                    continue
    except Exception as e:
        last_coupon_date = None

    # Coupon win check
    can_win_coupon = True
    if last_coupon_date:
        days_passed = (datetime.datetime.now() - last_coupon_date).days
        if days_passed < 14:  # 2 weeks = 14 days
            can_win_coupon = False
            print(f"\n{days_passed} days have passed since your last coupon. You need to wait {14-days_passed} more days for a new coupon.")

    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = '🍎'  # User is Apple, computer is Banana
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
            # Horizontal check
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                    self.winner = self.board[i][0]
                    return True
            
            # Vertical check
            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                    self.winner = self.board[0][i]
                    return True
            
            # Diagonal check
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                self.winner = self.board[0][0]
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                self.winner = self.board[0][2]
                return True
            
            # Draw check
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
    
    game = TicTacToe()
    win_count = 0
    
    # Get current score
    try:
        with open(file_dict['scoreboard'], 'r', encoding='utf-8') as f:
            scores = f.readlines()
        for line in scores:
            parts = line.strip().split(',')
            if len(parts) > 1 and parts[0] == username:
                win_count = int(parts[1])
    except:
        win_count = 0
    
    while not game.game_over:
        game.print_board()
        
        if game.current_player == '🍎':
            print("Your turn! (Enter a number between 1-9)")
            try:
                move = int(input("Your move: ")) - 1
                row = move // 3
                col = move % 3
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if game.make_move(row, col):
                        if game.check_winner():
                            game.game_over = True
                        else:
                            game.current_player = '🍌'
                    else:
                        print("Invalid move! Please select an empty square.")
                else:
                    print("Invalid move! Please enter a number between 1-9.")
            except ValueError:
                print("Invalid input! Please enter a number between 1-9.")
        else:
            print("Computer is thinking...")
            time.sleep(1)
            best_move = game.get_best_move()
            if best_move:
                row, col = best_move
                game.make_move(row, col)
                if game.check_winner():
                    game.game_over = True
                else:
                    game.current_player = '🍎'
    
    game.print_board()
    
    if game.winner == '🍎':
        print("Congratulations! You won!")
        win_count += 1
        update_score(username, 1)
        
        # Coupon check and add
        if can_win_coupon:
            # Check user's total coupon count
            total_coupons = 0
            try:
                with open(file_dict['coupons'], 'r', encoding='utf-8') as f:
                    coupons = f.readlines()
                for line in coupons:
                    if line.startswith(username + ','):
                        total_coupons += 1
            except:
                pass

            # Determine discount rate (decreasing rate)
            if total_coupons == 0:
                coupon_rate = 50  # First coupon 50%
            elif total_coupons == 1:
                coupon_rate = 35  # Second coupon 35%
            elif total_coupons == 2:
                coupon_rate = 25  # Third coupon 25%
            else:
                coupon_rate = 15  # Next coupons 15%

            # Save coupon
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            with open(file_dict['coupons'], 'a', encoding='utf-8') as f:
                f.write(f"{username},{coupon_rate},{today}\n")
            print(f"\nCongratulations! You won a %{coupon_rate} discount coupon!")
        else:
            print("\nYour score increased by 1!")
    elif game.winner == '🍌':
        print("Computer won!")
        win_count = 0  # Reset win count on loss
        update_score(username, -1)
    else:
        print("Draw!")
        update_score(username, 0)
    
    input("\nPress Enter to continue...")
    customer_menu(username)

def update_score(username, result):
    try:
        with open(file_dict['scoreboard'], 'r', encoding='utf-8') as f:
            scores = f.readlines()
    except:
        scores = []
    
    new_scores = []
    found = False
    
    for line in scores:
        parts = line.strip().split(',')
        if len(parts) > 2 and parts[0] == username:
            score = int(parts[1]) + result
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_scores.append(f"{username},{score},{date}\n")
            found = True
        else:
            new_scores.append(line)
    
    if not found:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        new_scores.append(f"{username},{result},{date}\n")
    
    with open(file_dict['scoreboard'], 'w', encoding='utf-8') as f:
        for line in new_scores:
            f.write(line)

def customer_minigame_scoreboard(username):
    clear()
    print("\n--- Minigame Scoreboard ---")
    try:
        with open(file_dict['scoreboard'], 'r', encoding='utf-8') as f:
            scores = f.readlines()
        
        if not scores:
            print("No scores yet!")
        else:
            # Sort scores from highest to lowest
            score_list = []
            for line in scores:
                parts = line.strip().split(',')
                if len(parts) > 2:
                    score_list.append((parts[0], int(parts[1]), parts[2]))
            
            # Sort scores from highest to lowest
            score_list.sort(key=lambda x: x[1], reverse=True)
            
            print("\nRank  Username        Score    Last Game")
            print("-" * 45)
            for i, (user, score, date) in enumerate(score_list, 1):
                print(f"{i:<5} {user:<15} {score:<8} {date}")
    except Exception as e:
        print(f"An error occurred! Error: {str(e)}")
    
    input("\nPress Enter to continue...")
    customer_minigame_menu(username)

def admin_login_menu():
    clear()
    print("\n--- Admin Login ---")
    admin_name = input("Admin Name: ")
    password = input("Password: ")
    
    try:
        with open(file_dict['admin'], 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        login_successful = False
        for line in lines:
            info = line.strip().split(',')
            if len(info) >= 2:  # At least 2 pieces of info (admin name and password)
                if info[0] == admin_name and info[1] == password:
                    login_successful = True
                    break
        
        if login_successful:
            print("Admin login successful!")
            wait_after_operation()
            admin_menu(admin_name)
        else:
            print("Wrong admin name or password!")
            wait_after_operation()
            main_menu()
    except Exception as e:
        print(f"An error occurred! Error: {str(e)}")
        wait_after_operation()
        main_menu()

def admin_menu(admin_name):
    clear()
    print(f"\n--- Admin Menu for {admin_name} ---")
    print("1. Most Purchased")
    print("2. View/Update Stock")
    print("3. Expiry/Decay Tracking")
    print("0. Back")
    choice = input("Select an option: ")
    if choice == '1':
        admin_most_purchased()
    elif choice == '2':
        admin_view_update_stock()
    elif choice == '3':
        admin_product_decay_tracking()
    elif choice == '0':
        main_menu()
    else:
        print("Invalid selection!")
        input("\nPress Enter to continue...")
        admin_menu(admin_name)

def admin_most_purchased():
    clear()
    print("\n--- Most Purchased Products ---")
    product_counter = {}
    with open(file_dict['purchases'], 'r', encoding='utf-8') as f:
        purchases = f.readlines()
    for line in purchases:
        parts = line.strip().split(',')
        if len(parts) > 3:
            product = parts[1]
            quantity = int(parts[2])
            if product in product_counter:
                product_counter[product] += quantity
            else:
                product_counter[product] = quantity
    
    # Sort by majority vote
    sorted_products = sorted(product_counter.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost Purchased Products (Sorted):")
    print("-" * 40)
    for i, (product, quantity) in enumerate(sorted_products, 1):
        print(f"{i}. {product}: {quantity} units")
    
    # Save this ranking to stock file
    with open(file_dict['stock'], 'r', encoding='utf-8') as f:
        stocks = f.readlines()
    
    new_stocks = []
    for line in stocks:
        parts = line.strip().split(',')
        if len(parts) > 2:
            product = parts[1]
            # Add ranking information
            ranking = next((i for i, (p, _) in enumerate(sorted_products, 1) if p == product), 0)
            if ranking > 0:
                parts.append(str(ranking))
            new_stocks.append(','.join(parts) + '\n')
        else:
            new_stocks.append(line)
    
    with open(file_dict['stock'], 'w', encoding='utf-8') as f:
        for line in new_stocks:
            f.write(line)
    
    input("\nPress Enter to continue...")
    admin_menu('admin')

def admin_view_update_stock():
    clear()
    print("\n--- View/Update Stock ---")
    print("1. View Stock")
    print("2. Update Stock")
    print("0. Back")
    choice = input("Select an option: ")
    if choice == '1':
        print("\nCurrent Stock:")
        with open(file_dict['stock'], 'r', encoding='utf-8') as f:
            stocks = f.readlines()
        for line in stocks:
            parts = line.strip().split(',')
            if len(parts) > 2:
                print(f"Product: {parts[1]}, Stock: {parts[2]}")
    elif choice == '2':
        print("\nUpdate Stock:")
        product = input("Enter product name: ")
        quantity = input("Enter new stock quantity: ")
        if not quantity.isdigit() or int(quantity) < 0:
            print("Invalid stock format!")
            input("\nPress Enter to continue...")
            admin_menu('admin')
            return
        quantity = int(quantity)
        new_stocks = []
        with open(file_dict['stock'], 'r', encoding='utf-8') as f:
            stocks = f.readlines()
        product_found = False
        for line in stocks:
            parts = line.strip().split(',')
            if len(parts) > 2 and parts[1] == product:
                parts[2] = str(quantity)
                product_found = True
            new_stocks.append(','.join(parts) + '\n')
        if not product_found:
            print(f"\nProduct not found!")
        else:
            with open(file_dict['stock'], 'w', encoding='utf-8') as f:
                for line in new_stocks:
                    f.write(line)
            print(f"\nStock updated successfully!")
    elif choice == '0':
        admin_menu('admin')
        return
    else:
        print("Invalid selection!")
    input("\nPress Enter to continue...")
    admin_view_update_stock()

def admin_product_decay_tracking():
    clear()
    print("\n--- Expiry/Decay Tracking ---")
    
    try:
        with open(file_dict['stock'], 'r', encoding='utf-8') as f:
            stocks = f.readlines()
    except:
        print("No stock data found!")
        wait_after_operation()
        admin_menu('admin')
        return
    
    # Product decay periods (days)
    decay_periods = {
        'Apple': 30,
        'Banana': 7,
        'Orange': 14,
        'Tomato': 5,
        'Cucumber': 7
    }
    
    today = datetime.datetime.now().date()
    warning_products = []
    
    print("\nDecay Tracking:")
    print("-" * 60)
    print(f"{'Product':<15} {'Quantity':<10} {'Decay Date':<15} {'Days Left':<10}")
    print("-" * 60)
    
    for line in stocks:
        parts = line.strip().split(',')
        if len(parts) > 2:
            product = parts[1]
            quantity = int(parts[2])
            
            if product in decay_periods:
                decay_period = decay_periods[product]
                decay_date = today + datetime.timedelta(days=decay_period)
                days_left = (decay_date - today).days
                
                print(f"{product:<15} {quantity:<10} {decay_date.strftime('%Y-%m-%d'):<15} {days_left:<10}")
                
                if days_left <= 3:
                    warning_products.append((product, quantity, decay_date, days_left))
    
    if warning_products:
        print("\nWARNING: The following products will decay soon!")
        for product, quantity, date, days in warning_products:
            print(f"{product}: {quantity} units - {days} days left!")
    else:
        print("\nAll products are fresh!")
    
    wait_after_operation()
    admin_menu('admin')

# Start the program
main_menu()
