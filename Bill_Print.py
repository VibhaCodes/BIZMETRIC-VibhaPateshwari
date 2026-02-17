####
# 1. USING IF-ELSE FUNCTION:
####

sr_num = input("Enter serial number: ")
menu = input("Enter the menu : ")
quantity = int(input("Enter the quantity: "))
price = int(input("Enter the price: "))

# Bill content
line = "----------------------------------------------------"

bill_text = ""
bill_text += "{:^50}\n".format(line)
bill_text += "{:^50}\n".format(":Welcome to Shiv Sagar:")
bill_text += "{:^50}\n".format(line)

bill_text += "{:2} {:^8} {:^15} {:^20}\n".format('SrNo.','Menu', 'Quantity', 'Price')
bill_text += "{0:2} {1:^14} {2:^8} {3:^27}\n".format(sr_num, menu, quantity, price)

bill_text += "\n"
bill_text += "{:^50}\n".format(line)
bill_text += "Total amount: {}\n".format(quantity * price)
bill_text += "{:^50}\n".format(line)

# Print on screen
print(bill_text)


##############
#### 2. USING FUNCTIONS
##############

# # 
# take order and store in dict
# deliver the order
# generate bill
# print the bill

class Restaurant:

    def __init__(self, name):
        self.name = name
        self.orders = {}   # dictionary to store order

    def take_order(self, sr_num, menu, quantity, price):
        self.orders["SrNo"] = sr_num
        self.orders["Menu"] = menu
        self.orders["Quantity"] = quantity
        self.orders["Price"] = price

    def generate_bill(self):
        line = "-" * 50
        total = self.orders["Quantity"] * self.orders["Price"]

        bill_text = ""
        bill_text += f"{line:^50}\n"
        bill_text += f"{':Welcome to ' + self.name + ':':^50}\n"
        bill_text += f"{line:^50}\n"

        bill_text += "{:2} {:^8} {:^15} {:^20}\n".format(
            'SrNo.', 'Menu', 'Quantity', 'Price'
        )

        bill_text += "{0:2} {1:^14} {2:^8} {3:^27}\n".format(
            self.orders["SrNo"],
            self.orders["Menu"],
            self.orders["Quantity"],
            self.orders["Price"]
        )

        bill_text += "\n"
        bill_text += f"{line:^50}\n"
        bill_text += f"Total amount: {total}\n"
        bill_text += f"{line:^50}\n"

        return bill_text


# -------------------------------
# Using the class
# -------------------------------

hotel = Restaurant("Shiv Sagar")

sr_num = input("Enter serial number: ")
menu = input("Enter the menu : ")
quantity = int(input("Enter the quantity: "))
price = int(input("Enter the price: "))

hotel.take_order(sr_num, menu, quantity, price)

print(hotel.generate_bill())



sr_num = input("Enter serial number: ")
menu = input("Enter the menu : ")
quantity = int(input("Enter the quantity: "))
price = int(input("Enter the price: "))


# 
line = "----------------------------------------------------"

bill_text = ""
bill_text += "{:^50}\n".format(line)
bill_text += "{:^50}\n".format(":Welcome to Shiv Sagar:")
bill_text += "{:^50}\n".format(line)

bill_text += "{:2} {:^8} {:^15} {:^20}\n".format('SrNo.','Menu', 'Quantity', 'Price')
bill_text += "{0:2} {1:^14} {2:^8} {3:^27}\n".format(sr_num, menu, quantity, price)

bill_text += "\n"
bill_text += "{:^50}\n".format(line)
bill_text += "Total amount: {}\n".format(quantity * price)
bill_text += "{:^50}\n".format(line)

print(bill_text)









####
## 3. USING DATABASE
####

import sqlite3
from datetime import datetime


DB_NAME = "restaurant.db"


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.seed_menu()  

    
    def create_tables(self):
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                menu_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                total_amount REAL NOT NULL,
                order_time TEXT NOT NULL,
                FOREIGN KEY(menu_id) REFERENCES menu(id)
            )
        """)
        self.conn.commit()

    def seed_menu(self):
        items = [
            ("Dosa", 80),
            ("Idli", 50),
            ("Vada", 40),
            ("Poha", 35),
            ("Tea", 20),
            ("Coffee", 30)
        ]

        for name, price in items:
            self.cursor.execute("""
                INSERT OR IGNORE INTO menu (name, price)
                VALUES (?, ?)
            """, (name.lower(), price))

        self.conn.commit()

    
    def show_menu(self):
        print("\n----- MENU -----")
        self.cursor.execute("SELECT id, name, price FROM menu")
        rows = self.cursor.fetchall()
        for r in rows:
            print(f"{r[0]}. {r[1].title()} - ₹{r[2]}")
        print("----------------\n")

    def get_menu_item(self, menu_name):
        self.cursor.execute("""
            SELECT id, name, price
            FROM menu
            WHERE name = ?
        """, (menu_name.lower(),))
        return self.cursor.fetchone()  

    
    def take_order(self, menu_name, quantity):
        item = self.get_menu_item(menu_name)
        if item is None:
            print("Menu item not found. Please choose from menu.")
            return None

        menu_id, name, price = item
        total = price * quantity

        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("""
            INSERT INTO orders (menu_id, quantity, price, total_amount, order_time)
            VALUES (?, ?, ?, ?, ?)
        """, (menu_id, quantity, price, total, order_time))

        self.conn.commit()

        order_id = self.cursor.lastrowid  

        return {
            "order_id": order_id,
            "menu_id": menu_id,
            "menu_name": name,
            "quantity": quantity,
            "price": price,
            "total_amount": total,
            "order_time": order_time
        }

    def generate_bill_text(self, order):
        line = "-" * 50
        bill = ""

        bill += f"{line}\n"
        bill += f"{('Welcome to ' + self.name):^50}\n"
        bill += f"{line}\n"
        bill += f"Order ID: {order['order_id']}\n"
        bill += f"Time    : {order['order_time']}\n"
        bill += f"{line}\n"

        bill += "{:<10} {:<15} {:<10} {:<10}\n".format("MenuID", "Item", "Qty", "Price")
        bill += "{:<10} {:<15} {:<10} {:<10}\n".format(
            order["menu_id"],
            order["menu_name"].title(),
            order["quantity"],
            order["price"]
        )

        bill += f"{line}\n"
        bill += f"Total Amount: ₹{order['total_amount']}\n"
        bill += f"{line}\n"

        return bill

    def print_or_save_bill(self, bill_text):
        choice = input("Do you want to save bill to file? (yes/no): ").strip().lower()

        if choice == "yes":
            filename = f"bill_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w") as f:
                f.write(bill_text)
            print(f"Bill saved as: {filename}")
        else:
            print("\n" + bill_text)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    hotel = Restaurant("Shiv Sagar")

    hotel.show_menu()

    menu = input("Enter menu item name: ").strip()
    quantity = int(input("Enter quantity: "))

    order = hotel.take_order(menu, quantity)

    if order:
        bill_text = hotel.generate_bill_text(order)
        hotel.print_or_save_bill(bill_text)

    hotel.close()









