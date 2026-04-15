from config import Config
import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        database=Config.DB_NAME,
        ssl_ca=Config.SSL_CA,
        ssl_disabled=False
    )
    return conn