# 3. Online Banking Transaction Analyzer
### Problem Statement
# A bank stores transactions in SQLite.
# Each transaction contains:
# * Transaction ID
# * Account Number
# * Amount
# * Date
# * Type (Credit/Debit)
# ### Requirements
# 1. Retrieve all transactions.
# 2. Sort them by amount using **Quick Sort**.
# 3. Search transactions using Transaction ID.
# 4. Calculate total credits and debits.
# 5. Display the top 5 highest-value transactions.
# ### Concepts
# * SQL
# * Quick Sort
# * Binary Search
# * Aggregation
import sqlite3
# Transaction Class
class Transaction:
    def __init__(self, tid, account, amount, date, ttype):
        self.tid = tid
        self.account = account
        self.amount = amount
        self.date = date
        self.ttype = ttype
    def display(self):
        print("-" * 45)
        print("Transaction ID :", self.tid)
        print("Account Number :", self.account)
        print("Amount         :", self.amount)
        print("Date           :", self.date)
        print("Type           :", self.ttype)
# Create Database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY,
    account_number TEXT,
    amount REAL,
    date TEXT,
    type TEXT
)
""")
# Delete old records
cursor.execute("DELETE FROM transactions")
# Insert Sample Data
data = [
    (1001, "ACC101", 2500, "2026-07-01", "Credit"),
    (1002, "ACC102", 1800, "2026-07-02", "Debit"),
    (1003, "ACC103", 5000, "2026-07-03", "Credit"),
    (1004, "ACC104", 700, "2026-07-04", "Debit"),
    (1005, "ACC105", 9500, "2026-07-05", "Credit"),
    (1006, "ACC106", 4300, "2026-07-06", "Debit"),
    (1007, "ACC107", 6200, "2026-07-07", "Credit"),
    (1008, "ACC108", 1200, "2026-07-08", "Debit"),
    (1009, "ACC109", 7800, "2026-07-09", "Credit"),
    (1010, "ACC110", 3100, "2026-07-10", "Debit")
]
cursor.executemany("INSERT INTO transactions VALUES (?,?,?,?,?)", data)
conn.commit()
# Fetch Transactions
cursor.execute("SELECT * FROM transactions")
rows = cursor.fetchall()
transactions = []
for row in rows:
    transactions.append(Transaction(*row))
# Quick Sort
def partition(arr, low, high):
    pivot = arr[high].amount
    i = low - 1
    for j in range(low, high):
        if arr[j].amount <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
quick_sort(transactions, 0, len(transactions) - 1)
print("\nTransactions Sorted by Amount\n")
for t in transactions:
    t.display()
# Binary Search
transactions.sort(key=lambda x: x.tid)
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].tid == key:
            return arr[mid]
        elif arr[mid].tid < key:
            low = mid + 1
        else:
            high = mid - 1
    return None
tid = int(input("\nEnter Transaction ID to Search: "))
result = binary_search(transactions, tid)
if result:
    print("\nTransaction Found")
    result.display()
else:
    print("\nTransaction Not Found")
# Total Credits and Debits
total_credit = 0
total_debit = 0
for t in transactions:
    if t.ttype == "Credit":
        total_credit += t.amount
    else:
        total_debit += t.amount
print("\nTotal Credit :", total_credit)
print("Total Debit  :", total_debit)
# Top 5 Highest Transactions
transactions.sort(key=lambda x: x.amount, reverse=True)
print("\nTop 5 Highest Value Transactions\n")
for t in transactions[:5]:
    t.display()
conn.close()