import tkinter as tk
from tkinter import messagebox, ttk

# Data storage (in-memory for simplicity)
inventory = {}

# Functions for managing inventory
def add_product():
    name = entry_name.get().strip()
    try:
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive values.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return
    
    if name in inventory:
        messagebox.showerror("Error", "Product already exists!")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        messagebox.showinfo("Success", "Product added successfully!")
        clear_fields()
        view_inventory()

def update_product():
    name = entry_name.get().strip()
    try:
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive values.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    if name not in inventory:
        messagebox.showerror("Error", "Product not found!")
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        messagebox.showinfo("Success", "Product updated successfully!")
        clear_fields()
        view_inventory()

def remove_product():
    name = entry_name.get().strip()
    
    if name not in inventory:
        messagebox.showerror("Error", "Product not found!")
    else:
        del inventory[name]
        messagebox.showinfo("Success", "Product removed successfully!")
        clear_fields()
        view_inventory()

def view_inventory():
    for row in tree.get_children():
        tree.delete(row)
    
    for name, details in inventory.items():
        tree.insert('', 'end', values=(name, details['quantity'], details['price']))

def check_stock():
    low_stock_items = [name for name, details in inventory.items() if details['quantity'] < 5]
    
    if low_stock_items:
        messagebox.showwarning("Low Stock", f"Items running low: {', '.join(low_stock_items)}")
    else:
        messagebox.showinfo("Stock Check", "All items have sufficient stock.")

def calculate_total_value():
    total_value = sum(details['quantity'] * details['price'] for details in inventory.values())
    messagebox.showinfo("Total Inventory Value", f"Total inventory value: ${total_value:.2f}")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Colors for a visually appealing layout
bg_color = "#f3f6fb"          # Light background color for the app
frame_bg = "#dde7f0"           # Light blue shade for frames
button_bg = "#4a90e2"          # Blue shade for buttons
button_fg = "white"            # White text on buttons
entry_bg = "#ffffff"           # White background for entry fields

# GUI setup
app = tk.Tk()
app.title("Grocery Store Management System")
app.geometry("650x500")
app.configure(bg=bg_color)

# Frames for layout
frame_top = tk.Frame(app, bg=frame_bg, pady=10, padx=20)
frame_top.pack(fill='x')

frame_middle = tk.Frame(app, bg=bg_color)
frame_middle.pack(fill='x', pady=10)

frame_bottom = tk.Frame(app, bg=frame_bg)
frame_bottom.pack(fill='x', pady=10, padx=20)

# Labels and Entries in top frame
tk.Label(frame_top, text="Product Name:", bg=frame_bg).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(frame_top, width=25, bg=entry_bg)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_top, text="Quantity:", bg=frame_bg).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_quantity = tk.Entry(frame_top, width=25, bg=entry_bg)
entry_quantity.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_top, text="Price:", bg=frame_bg).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_price = tk.Entry(frame_top, width=25, bg=entry_bg)
entry_price.grid(row=2, column=1, padx=10, pady=5)

# Buttons in middle frame
btn_add = tk.Button(frame_middle, text="Add Product", command=add_product, width=15, bg=button_bg, fg=button_fg)
btn_add.grid(row=0, column=0, padx=10, pady=5)

btn_update = tk.Button(frame_middle, text="Update Product", command=update_product, width=15, bg=button_bg, fg=button_fg)
btn_update.grid(row=0, column=1, padx=10, pady=5)

btn_remove = tk.Button(frame_middle, text="Remove Product", command=remove_product, width=15, bg=button_bg, fg=button_fg)
btn_remove.grid(row=0, column=2, padx=10, pady=5)

btn_stock = tk.Button(frame_middle, text="Check Stock", command=check_stock, width=15, bg=button_bg, fg=button_fg)
btn_stock.grid(row=1, column=0, padx=10, pady=5)

btn_view = tk.Button(frame_middle, text="View Inventory", command=view_inventory, width=15, bg=button_bg, fg=button_fg)
btn_view.grid(row=1, column=1, padx=10, pady=5)

btn_total = tk.Button(frame_middle, text="Total Inventory Value", command=calculate_total_value, width=15, bg=button_bg, fg=button_fg)
btn_total.grid(row=1, column=2, padx=10, pady=5)

# Inventory Display in bottom frame
tree = ttk.Treeview(frame_bottom, columns=("Product Name", "Quantity", "Price"), show="headings")
tree.heading("Product Name", text="Product Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.column("Product Name", width=200)
tree.column("Quantity", width=100)
tree.column("Price", width=100)
tree.pack(fill='x', padx=10, pady=10)

# Run the app
app.mainloop()
