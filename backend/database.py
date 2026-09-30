import sqlite3


DB_NAME = "ragenius.db"



# =========================
# Connection
# =========================

def get_connection():

    return sqlite3.connect(DB_NAME)




# =========================
# Create Tables
# =========================

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chats (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id TEXT,

            role TEXT,

            content TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )


    conn.commit()

    conn.close()




# =========================
# Save Message
# =========================

def save_message(session_id, role, content):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO chats
        (
            session_id,
            role,
            content
        )

        VALUES (?, ?, ?)

        """,
        (
            session_id,
            role,
            content
        )
    )


    conn.commit()

    conn.close()




# =========================
# Get One Chat History
# =========================

def get_messages(session_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            role,
            content

        FROM chats

        WHERE session_id=?

        ORDER BY id ASC

        """,
        (
            session_id,
        )
    )


    rows = cursor.fetchall()


    conn.close()



    return [

        {
            "role": row[0],
            "content": row[1]
        }

        for row in rows

    ]




# =========================
# Get All Conversations
# =========================

def get_all_sessions():

    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT DISTINCT session_id

        FROM chats

        ORDER BY id DESC

        """
    )



    rows = cursor.fetchall()


    conn.close()



    return [

        row[0]

        for row in rows

    ]