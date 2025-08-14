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

def manual_entry_as_example(table, values, data):
    placeholders = ",".join(["?"] * len(data[0]))
    cur.executemany(f"INSERT INTO {table} ({values}) VALUES({placeholders})", data)
    con.commit()

'''
manual_entry_as_example("item_types","type, price",[
    ('Laptop', 1100),
    ('Book', 50),
    ('Laptop Adapter', 55)
])
'''

'''
manual_entry_as_example("items","barcode, title, status, item_type_id",[
    ([REDACTED], 'Sheila Rae, the brave', 'LOST', 2),
    ([REDACTED], 'Computers and the world of the future.', 'LOST', 2),
    ([REDACTED], 'Dell Latitude 5530 Laptop', 'LOST', 1),
    ([REDACTED], 'Dell Latitude 5530 Laptop', 'LOST', 3),
    ([REDACTED], 'Dell Latitude 5520 ; 16 GB ; 15.6" display', 'LOST', 1),
    ([REDACTED], 'Dell Latitude 5520 ; 16 GB ; 15.6" display', 'LOST', 3)
])
'''