import mysql.connector

# Konfigurasi Database MySQL
db_config = {
    # Konfigurasi untuk Railway
    'host': 'mysql.railway.internal',
    'user': 'root',
    'password': 'qKaGVTELvdtlgvrUUGEsIueROwVXWHGG',
    'database': 'railway'

    # Konfigurasi untuk localhost
    # 'host': 'localhost',
    # 'user': 'root',
    # 'password': 'root',
    # 'database': 'deteksi_hoaks'
}

def get_db_connection():
    """Membuat dan mengembalikan koneksi ke database."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error saat koneksi ke MySQL: {err}")
        return None
    
