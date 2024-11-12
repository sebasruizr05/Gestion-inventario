from utils.db_utils import create_connection

# Verificar si un producto existe por ID
def product_exists(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(1) FROM products WHERE id = ?', (product_id,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

# Función para agregar un producto
def add_product(name, description, quantity, price, product_id):
    if product_exists(product_id):
        raise ValueError(f"El producto con el código {product_id} ya existe.")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (id, name, description, quantity, price)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_id, name, description, quantity, price))
    conn.commit()
    conn.close()

# Función para editar un producto
def update_product(product_id, name, description, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products
        SET name = ?, description = ?, quantity = ?, price = ?
        WHERE id = ?
    ''', (name, description, quantity, price, product_id))
    conn.commit()
    conn.close()

# Función para eliminar un producto
def delete_product(product_id):
    if not product_exists(product_id):
        raise ValueError(f"El producto con el código {product_id} no existe.")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Función para obtener todos los productos
def get_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, description, quantity, price FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_details(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product