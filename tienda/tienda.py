#libraries

import tkinter as tk
from tkinter import messagebox

# Definición de la clase Product
class Product:
    def __init__(self, name, department, price, stock):
        self.name = name
        self.department = department
        self.price = price
        self.stock = stock

    def __str__(self):
        status = "Available" if self.stock > 0 else "Out of stock"
        return f"Product: {self.name}, Department: {self.department}, Price (CAD): {self.price:.2f}, In stock: {self.stock} ({status})"

# Lista de inventario
inventory = []

# Función para añadir un producto al inventario
def add_product():
    name = name_entry.get()
    department = department_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()

    if not name or not department or not price or not stock:
        messagebox.showwarning("Input Error", "Please fill all the fields.")
        return

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showwarning("Input Error", "Price must be a valid number and stock must be an integer.")
        return

    product = Product(name, department, price, stock)
    inventory.append(product)
    update_inventory_display()
    clear_entries()

# Función para actualizar la visualización del inventario
def update_inventory_display():
    inventory_display.delete(1.0, tk.END)
    for product in inventory:
        inventory_display.insert(tk.END, str(product) + "\n")

# Función para limpiar los campos de entrada
def clear_entries():
    name_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Inventory Management System")

# Crear etiquetas y campos de entrada
tk.Label(root, text="Product Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Department:").grid(row=1, column=0)
department_entry = tk.Entry(root)
department_entry.grid(row=1, column=1)

tk.Label(root, text="Price (CAD):").grid(row=2, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1)

tk.Label(root, text="Stock:").grid(row=3, column=0)
stock_entry = tk.Entry(root)
stock_entry.grid(row=3, column=1)

# Crear el botón para añadir productos
add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.grid(row=4, columnspan=2)

# Crear el área de texto para mostrar el inventario
inventory_display = tk.Text(root, height=10, width=50)
inventory_display.grid(row=5, columnspan=2)

# Ejecutar el bucle principal de la ventana
root.mainloop()