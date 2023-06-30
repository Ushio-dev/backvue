from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# Ruta al archivo .env
#dotenv_path = os.path.join(os.path.dirname(__file__), 'app/.env')

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear una instancia de MySQL
mysql = MySQL()

# Configurar la conexión a MySQL utilizando las variables de entorno
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
app.config['MYSQL_PORT'] = int(os.getenv("MYSQL_PORT"))
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor']
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inicializar la conexión a MySQL
mysql.init_app(app)
