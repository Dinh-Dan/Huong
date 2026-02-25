import pymysql
import os

def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'skillrank'),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def query(sql, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            if sql.strip().upper().startswith('SELECT') or sql.strip().upper().startswith('SHOW'):
                return cursor.fetchall()
            else:
                conn.commit()
                return cursor
    finally:
        conn.close()

def query_one(sql, params=None):
    rows = query(sql, params)
    if isinstance(rows, list) and len(rows) > 0:
        return rows[0]
    return None

def execute(sql, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            conn.commit()
            return cursor
    finally:
        conn.close()

# Test connection on import
try:
    conn = get_connection()
    conn.close()
    print('MySQL connected successfully')
except Exception as e:
    print(f'MySQL connection error: {e}')
