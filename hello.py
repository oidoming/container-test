import os 
import sys
import time
import sqlite3


VALUE = os.environ['VALUE_KEY']

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect("file:mem1?mode=memory&cache=shared", uri=True)


def create_package_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS data (value text)"""

    cursor.execute(sql)
    conn.commit()


def insert_package(value: str, conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO data(value) VALUES(?)""", [value])
    conn.commit()


def select_package(value: str, conn: sqlite3.Connection) -> tuple:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE value=?", [value])
    return cursor.fetchone()


def main():
    try:        
        conn = get_connection()
        create_package_table(conn)
        while True:
            #print(VALUE)
            insert_package(VALUE, conn)
            #with open("log.txt", "a") as myfile:
            #    myfile.write(VALUE)
            val = select_package(VALUE, conn)
            print(val[0])
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == '__main__':
    main()
