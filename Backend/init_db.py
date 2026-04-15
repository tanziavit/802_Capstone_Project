from models.db import get_db_connection
from werkzeug.security import generate_password_hash

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Properties table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            location VARCHAR(100),
            size VARCHAR(50),
            price VARCHAR(50),
            features TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Contents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contents (
            id INT AUTO_INCREMENT PRIMARY KEY,
            property_id INT,
            content_type VARCHAR(50),
            text TEXT,
            tone VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tables created successfully")


def insert_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert user
    password = generate_password_hash("123456")

    cursor.execute("""
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s)
    """, ("Test User", "test@example.com", password))

    user_id = cursor.lastrowid

    # Insert property
    cursor.execute("""
        INSERT INTO properties (user_id, location, size, price, features)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        user_id,
        "Mumbai",
        "3 BHK",
        "₹1.2 Cr",
        "Sea view, Balcony, Parking"
    ))

    property_id = cursor.lastrowid

    # Insert content
    contents = [
        ("listing", "A premium 3 BHK apartment in Mumbai with sea view.", "professional"),
        ("social", "Dream home in Mumbai! 3 BHK with sea view", "casual"),
        ("email", "Dear Buyer, check out this 3 BHK in Mumbai...", "formal"),
        ("video", "Welcome to this beautiful Mumbai property...", "engaging")
    ]

    for ctype, text, tone in contents:
        cursor.execute("""
            INSERT INTO contents (property_id, content_type, text, tone)
            VALUES (%s, %s, %s, %s)
        """, (property_id, ctype, text, tone))

    conn.commit()
    cursor.close()
    conn.close()

    print("Sample data inserted successfully")


if __name__ == "__main__":
    create_tables()
    insert_sample_data()