import tkinter as tk
from tkinter import messagebox
from utils.config_manager import add_product, update_product, delete_product, get_all_products, get_product_details, product_exists, search_products

# Función para seleccionar el rol inicial
def role_selection_window():
    root = tk.Tk()
    root.title("Seleccionar Rol")
    root.geometry("300x200")

    tk.Label(root, text="Seleccione su rol", font=("Arial", 14)).pack(pady=20)

    admin_button = tk.Button(root, text="Administrador", command=lambda: open_main_window("admin", root))
    admin_button.pack(pady=10)

    client_button = tk.Button(root, text="Cliente", command=lambda: open_main_window("client", root))
    client_button.pack(pady=10)

    root.mainloop()

# Función para abrir la ventana principal con opciones según el rol
def open_main_window(role, root):
    root.destroy()  # Cierra la ventana de selección de rol
    main_window(role)

# Función para regresar a la pantalla de selección de rol
def go_back(root):
    root.destroy()
    role_selection_window()

# Función para mostrar la interfaz principal según el rol seleccionado
def main_window(role):
    global input_id, input_name, input_description, input_quantity, input_price, product_list, search_input, search_criteria
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("500x600")

    # Botón para regresar a la pantalla de selección de rol
    back_button = tk.Button(root, text="Regresar", command=lambda: go_back(root))
    back_button.pack(pady=5)

    if role == "admin":
        # Sección de entrada de datos (solo para administrador)
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

        # Botones de acción para administrador
        add_button = tk.Button(root, text="Agregar Producto", command=handle_add_product)
        add_button.pack(pady=5)

        edit_button = tk.Button(root, text="Editar Producto", command=handle_edit_product)
        edit_button.pack(pady=5)

        delete_button = tk.Button(root, text="Eliminar Producto", command=handle_delete_product)
        delete_button.pack(pady=5)

    # Sección de lista de productos (para ambos roles)
    tk.Label(root, text="Inventario de Productos").pack(pady=5)
    product_list = tk.Listbox(root, width=60)
    product_list.pack(pady=5)

    # Botón para ver detalles del producto (para ambos roles)
    detail_button = tk.Button(root, text="Ver Detalles del Producto", command=show_product_details)
    detail_button.pack(pady=5)

    if role == "client":
        # Campo de búsqueda y botón de búsqueda (solo para cliente)
        tk.Label(root, text="Buscar Producto").pack(pady=5)
        search_input = tk.Entry(root)
        search_input.pack(pady=5)

        # Selección de criterio de búsqueda (nombre o precio)
        search_criteria = tk.StringVar(value="name")
        tk.Radiobutton(root, text="Nombre", variable=search_criteria, value="name").pack()
        tk.Radiobutton(root, text="Precio menor a", variable=search_criteria, value="price").pack()

        search_button = tk.Button(root, text="Buscar", command=handle_search_product)
        search_button.pack(pady=5)

    # Botón para recargar la lista de productos (para ambos roles)
    load_button = tk.Button(root, text="Recargar Lista de Productos", command=load_products)
    load_button.pack(pady=5)

    # Cargar la lista al iniciar la aplicación
    load_products()

    root.mainloop()

# Función para manejar la búsqueda de productos
def handle_search_product():
    search_term = search_input.get()
    criteria = search_criteria.get()

    if not search_term:
        messagebox.showerror("Error", "Ingrese un término de búsqueda.")
        return

    # Convertir a número si el criterio es precio
    if criteria == 'price':
        try:
            search_term = float(search_term)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico para la búsqueda por precio.")
            return

    # Realizar la búsqueda según el criterio
    filtered_products = search_products(search_term, criteria)
    product_list.delete(0, tk.END)  # Borra la lista actual
    for product in filtered_products:
        product_list.insert(tk.END, f"ID: {product[0]}, Nombre: {product[1]}, Cantidad: {product[3]}, Precio: ${product[4]}")

# Manejar la adición de un producto con validación
def handle_add_product():
    try:
        product_id = int(input_id.get())
        name = input_name.get()
        description = input_description.get()
        quantity = int(input_quantity.get())
        price = float(input_price.get())

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
    product_list.delete(0, tk.END)
    for product in products:
        product_list.insert(tk.END, f"ID: {product[0]}, Nombre: {product[1]}, Cantidad: {product[3]}, Precio: ${product[4]}")

# Función para mostrar detalles del producto en una nueva ventana
def show_product_details():
    selected_product = product_list.curselection()
    if not selected_product:
        messagebox.showerror("Error", "Seleccione un producto de la lista para ver los detalles.")
        return

    product_index = selected_product[0]
    product_id = get_all_products()[product_index][0]
    product_details = get_product_details(product_id)

    detail_window = tk.Toplevel()
    detail_window.title("Detalles del Producto")
    detail_window.geometry("300x300")

    tk.Label(detail_window, text=f"ID: {product_details[0]}").pack(pady=5)
    tk.Label(detail_window, text=f"Nombre: {product_details[1]}").pack(pady=5)
    tk.Label(detail_window, text=f"Descripción: {product_details[2]}").pack(pady=5)
    tk.Label(detail_window, text=f"Cantidad: {product_details[3]}").pack(pady=5)
    tk.Label(detail_window, text=f"Precio: ${product_details[4]}").pack(pady=5)

# Iniciar la aplicación con la selección de rol
role_selection_window()