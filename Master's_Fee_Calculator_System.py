import os
import sqlite3
from datetime import datetime

desktop_path = "/Users/vibhapateshwari/Desktop/bill_printing"


conn = sqlite3.connect("bill.db")
cur = conn.cursor()


def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bill_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        analytics TEXT,
        hostel TEXT,
        food_months INTEGER,
        transport TEXT,
        total_cost REAL
    )
    """)
    conn.commit()



def calculate_total(subject, analytics, hostel, food_months, transport):
    total = 200000

    if (subject == "HR" or subject == "Marketing") and analytics == "Y":
        total = total + (200000 * 0.10)

    if hostel == "Y":
        total = total + 200000

    total = total + (food_months * 2000)

    total = total + (2 * 13000)

    return total



def generate_bill(subject, analytics, hostel, food_months, transport, total):
    line = "-" * 40

    bill = ""
    bill += line + "\n"
    bill += "MASTER'S FEE BILL\n"
    bill += line + "\n"
    bill += "Subject: " + subject + "\n"
    bill += "Analytics: " + analytics + "\n"
    bill += "Hostel: " + hostel + "\n"
    bill += "Food Months: " + str(food_months) + "\n"
    bill += "Transport: " + transport + "\n"
    bill += line + "\n"
    bill += "Total Annual Cost: ₹" + str(total) + "\n"
    bill += line + "\n"
    bill += "Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    bill += line + "\n"

    return bill



def save_bill_file(bill_text):
    filename = "Masters_Bill_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    full_path = os.path.join(desktop_path, filename)

    with open(full_path, "w") as f:
        f.write(bill_text)

    print("Bill saved at:", full_path)



def save_to_db(subject, analytics, hostel, food_months, transport, total):
    cur.execute(
        "INSERT INTO bill_records(subject, analytics, hostel, food_months, transport, total_cost) VALUES(?,?,?,?,?,?)",
        (subject, analytics, hostel, food_months, transport, total)
    )
    conn.commit()
    print("Data saved in Database")



create_table()

subject = input("Enter subject (HR/Finance/Marketing/DS): ")
analytics = input("Analytics (Y/N): ")
hostel = input("Hostel (Y/N): ")
food_months = int(input("Food months: "))
transport = input("Transport (semester/annual): ")

total = calculate_total(subject, analytics, hostel, food_months, transport)

bill_text = generate_bill(subject, analytics, hostel, food_months, transport, total)

print("\n" + bill_text)

save_bill_file(bill_text)

save_to_db(subject, analytics, hostel, food_months, transport, total)

conn.close()