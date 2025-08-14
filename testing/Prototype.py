import sqlite3

con = sqlite3.connect("example/prototype.db")
cur = con.cursor()

def create_tables():
    cur.execute("PRAGMA foreign_keys = ON;")

    cur.execute("""
        CREATE TABLE item_types(
            item_type_id INTEGER PRIMARY KEY,
            type VARCHAR(32),
            price DECIMAL(5, 2)
        )
    """)

    cur.execute("""
        CREATE TABLE items (
            item_id INTEGER PRIMARY KEY,
            barcode VARCHAR(32),
            title TEXT NOT NULL,
            status TINYBLOB,
            item_type_id INTEGER,
            FOREIGN KEY (item_type_id) REFERENCES item_types(item_type_id)
        )
    """)

    cur.execute("""
        CREATE TABLE patrons (
            patron_id INTEGER PRIMARY KEY,
            eagle_id VARCHAR(32),
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            preferred_email VARCHAR(100)
        )
    """)

    cur.execute("""
        CREATE TABLE transactions (
            transaction_id INTEGER PRIMARY KEY,
            item_id INTEGER NOT NULL,
            process_status VARCHAR(8) NOT NULL DEFAULT 'LOST' CHECK (process_status IN ('LOST','RETURNED')),
            process_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            patron_id INTEGER NOT NULL,
            loan_date DATE,
            due_date DATE,
            FOREIGN KEY (item_id) REFERENCES items(item_id),
            FOREIGN KEY (patron_id) REFERENCES patrons(patron_id)
        )
    """)


create_tables()