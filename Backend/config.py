import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

    # Azure MySQL Config
    DB_HOST = os.getenv("DB_HOST", "realestatedb.mysql.database.azure.com")
    DB_USER = os.getenv("DB_USER", "adminuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "realestate_db")
    DB_PORT = 3306

    # SSL Certificate Path
    SSL_CA = os.getenv("SSL_CA", "DigiCertGlobalRootG2.crt.pem")

    # Hugging Face API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")