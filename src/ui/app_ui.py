import tkinter as tk
from tkinter import messagebox
from utils.config_manager import add_product, update_product, delete_product, get_all_products, product_exists

# Manejar la adición de un producto con validación
def handle_add_product():
    try:
        product_id = int(input_id.get())
        name = input_name.get()
        description = input_description.get()
        quantity = int(input_quantity.get())
        price = float(input_price.get())

        # Validación para verificar si el producto ya existe
        if product_exists(product_id):
            messagebox.showerror("Error", f"El producto con ID {product_id} ya existe.")
        else:
            add_product(name, description, quantity, price, product_id)
            messagebox.showinfo("Info", "Producto agregado correctamente")
            load_products()
    except ValueError as e:
        messagebox.showerror("Error", f"Error en la entrada de datos: {str(e)}")

# Manejar la edición de un producto existente
def handle_edit_product():
    try:
        product_id = int(input_id.get())
        name = input_name.get()
        description = input_description.get()
        quantity = int(input_quantity.get())
        price = float(input_price.get())
        update_product(product_id, name, description, quantity, price)
        messagebox.showinfo("Info", "Producto editado correctamente")
        load_products()
    except ValueError as e:
        messagebox.showerror("Error", f"Error en la entrada de datos: {str(e)}")

# Manejar la eliminación de un producto con validación
def handle_delete_product():
    try:
        product_id = int(input_id.get())

        # Validación para verificar si el producto existe antes de eliminarlo
        if not product_exists(product_id):
            messagebox.showerror("Error", f"El producto con ID {product_id} no existe.")
        else:
            delete_product(product_id)
            messagebox.showinfo("Info", "Producto eliminado correctamente")
            load_products()
    except ValueError as e:
        messagebox.showerror("Error", f"Error en la entrada de datos: {str(e)}")

# Función para cargar todos los productos en el Listbox
def load_products():
    products = get_all_products()
    product_list.delete(0, tk.END)  # Borra la lista actual
    for product in products:
        product_list.insert(tk.END, f"ID: {product[0]}, Nombre: {product[1]}, Cantidad: {product[3]}, Precio: ${product[4]}")

# Configuración de la ventana principal
def main_window():
    global input_id, input_name, input_description, input_quantity, input_price, product_list
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("500x500")

    # Sección de entrada de datos
    tk.Label(root, text="ID de Producto (para agregar/editar/eliminar)").pack(pady=5)
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