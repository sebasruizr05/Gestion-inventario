from utils.db_utils import create_connection

# Función para agregar un producto
def add_product(name, description, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, description, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, description, quantity, price))
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