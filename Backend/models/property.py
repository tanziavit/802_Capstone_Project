from models.db import get_db_connection

class Property:

    @staticmethod
    def create(user_id, location, size, price, features):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO properties (user_id, location, size, price, features)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, location, size, price, features))

        conn.commit()
        property_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return property_id

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT * FROM properties WHERE user_id = %s ORDER BY id DESC
        """, (user_id,))

        properties = cursor.fetchall()

        cursor.close()
        conn.close()

        return properties