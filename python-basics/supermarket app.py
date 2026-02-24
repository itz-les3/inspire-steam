#Name: Mark Leslie
#Date: 24/02/2026

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("supermarket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    total REAL
)
""")

conn.commit()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Supermarket POS System")
root.geometry("700x500")

cart = []
total_amount = 0


# ---------------- FUNCTIONS ----------------

def add_product():
    name = entry_name.get()
    price = entry_price.get()
    stock = entry_stock.get()

    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                   (name, price, stock))
    conn.commit()
    messagebox.showinfo("Success", "Product Added Successfully")

def add_to_cart():
    global total_amount
    product_name = entry_sale_name.get()
    quantity = int(entry_sale_qty.get())

    cursor.execute("SELECT price, stock FROM products WHERE name=?",
                   (product_name,))
    result = cursor.fetchone()

    if result:
        price, stock = result
        if quantity <= stock:
            total = price * quantity
            total_amount += total
            cart.append((product_name, quantity, total))

            cursor.execute("UPDATE products SET stock=? WHERE name=?",
                           (stock - quantity, product_name))
            conn.commit()

            update_cart_display()
        else:
            messagebox.showerror("Error", "Not enough stock")
    else:
        messagebox.showerror("Error", "Product not found")

def update_cart_display():
    listbox.delete(0, tk.END)
    for item in cart:
        listbox.insert(tk.END, f"{item[0]}  x{item[1]}  = {item[2]}")
    label_total.config(text=f"Total: {total_amount}")

def complete_sale():
    global cart, total_amount

    for item in cart:
        cursor.execute("INSERT INTO sales (product, quantity, total) VALUES (?, ?, ?)",
                       item)
    conn.commit()

    messagebox.showinfo("Success", "Sale Completed")
    cart = []
    total_amount = 0
    update_cart_display()

# ---------------- UI ----------------

frame_inventory = tk.LabelFrame(root, text="Add Product")
frame_inventory.pack(fill="x", padx=10, pady=5)

tk.Label(frame_inventory, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame_inventory)
entry_name.grid(row=0, column=1)

tk.Label(frame_inventory, text="Price").grid(row=0, column=2)
entry_price = tk.Entry(frame_inventory)
entry_price.grid(row=0, column=3)

tk.Label(frame_inventory, text="Stock").grid(row=0, column=4)
entry_stock = tk.Entry(frame_inventory)
entry_stock.grid(row=0, column=5)

tk.Button(frame_inventory, text="Add Product", command=add_product).grid(row=0, column=6)


frame_sales = tk.LabelFrame(root, text="Sales")
frame_sales.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(frame_sales, text="Product Name").grid(row=0, column=0)
entry_sale_name = tk.Entry(frame_sales)
entry_sale_name.grid(row=0, column=1)

tk.Label(frame_sales, text="Quantity").grid(row=0, column=2)
entry_sale_qty = tk.Entry(frame_sales)
entry_sale_qty.grid(row=0, column=3)

tk.Button(frame_sales, text="Add to Cart", command=add_to_cart).grid(row=0, column=4)

listbox = tk.Listbox(frame_sales, width=80)
listbox.grid(row=1, column=0, columnspan=5)

label_total = tk.Label(frame_sales, text="Total: 0", font=("Arial", 14))
label_total.grid(row=2, column=0)

tk.Button(frame_sales, text="Complete Sale", command=complete_sale).grid(row=2, column=4)

root.mainloop()
