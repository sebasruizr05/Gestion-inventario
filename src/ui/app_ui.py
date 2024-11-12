import tkinter as tk
from tkinter import messagebox
from utils.config_manager import add_product, update_product, delete_product, get_all_products

def handle_add_product():
    name = input_name.get()
    description = input_description.get()
    quantity = int(input_quantity.get())
    price = float(input_price.get())
    add_product(name, description, quantity, price)
    messagebox.showinfo("Info", "Producto agregado correctamente")
    load_products()

def handle_edit_product():
    product_id = int(input_id.get())
    name = input_name.get()
    description = input_description.get()
    quantity = int(input_quantity.get())
    price = float(input_price.get())
    update_product(product_id, name, description, quantity, price)
    messagebox.showinfo("Info", "Producto editado correctamente")
    load_products()

def handle_delete_product():
    product_id = int(input_id.get())
    delete_product(product_id)
    messagebox.showinfo("Info", "Producto eliminado correctamente")
    load_products()

# Función para cargar todos los productos en el Listbox
def load_products():
    products = get_all_products()
    product_list.delete(0, tk.END)  # Borra la lista actual
    for product in products:
        product_list.insert(tk.END, f"ID: {product[0]}, Nombre: {product[1]}, Cantidad: {product[3]}, Precio: ${product[4]}")

def main_window():
    global input_id, input_name, input_description, input_quantity, input_price, product_list
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("500x500")

    # Sección de entrada de datos
    tk.Label(root, text="ID de Producto (para editar/eliminar)").pack(pady=5)
    input_id = tk.Entry(root)
    input_id.pack(pady=5)

    tk.Label(root, text="Nombre de Producto").pack(pady=5)
    input_name = tk.Entry(root)
    input_name.pack(pady=5)

    tk.Label(root, text="Descripción de Producto").pack(pady=5)
    input_description = tk.Entry(root)
    input_description.pack(pady=5)

    tk.Label(root, text="Cantidad").pack(pady=5)
    input_quantity = tk.Entry(root)
    input_quantity.pack(pady=5)

    tk.Label(root, text="Precio").pack(pady=5)
    input_price = tk.Entry(root)
    input_price.pack(pady=5)

    # Botones de acción
    add_button = tk.Button(root, text="Agregar Producto", command=handle_add_product)
    add_button.pack(pady=5)

    edit_button = tk.Button(root, text="Editar Producto", command=handle_edit_product)
    edit_button.pack(pady=5)

    delete_button = tk.Button(root, text="Eliminar Producto", command=handle_delete_product)
    delete_button.pack(pady=5)

    # Sección de lista de productos
    tk.Label(root, text="Inventario de Productos").pack(pady=5)
    product_list = tk.Listbox(root, width=60)
    product_list.pack(pady=5)

    # Botón para recargar la lista de productos
    load_button = tk.Button(root, text="Recargar Lista de Productos", command=load_products)
    load_button.pack(pady=5)

    # Cargar la lista al iniciar la aplicación
    load_products()

    root.mainloop()