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