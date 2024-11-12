from ui.app_ui import main_window
from utils.db_utils import create_table

# Crear la tabla al iniciar la aplicación
create_table()

# Ejecutar la interfaz principal
if __name__ == "__main__":
    main_window()

