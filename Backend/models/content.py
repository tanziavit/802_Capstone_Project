from models.db import get_db_connection

class Content:

    @staticmethod
    def create(property_id, content_type, text, tone):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO contents (property_id, content_type, text, tone)
            VALUES (%s, %s, %s, %s)
        """, (property_id, content_type, text, tone))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def get_by_property(property_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT * FROM contents WHERE property_id = %s
        """, (property_id,))

        contents = cursor.fetchall()

        cursor.close()
        conn.close()

        return contents