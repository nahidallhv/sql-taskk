import sqlite3
connection = sqlite3.connect("computer_parts")
cursor = connection.cursor()
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        manufacturer TEXT,
        price REAL)""")
    connection.commit()
def add_data():
    cursor.execute("INSERT INTO parts (name, type, manufacturer, price) VALUES ('CPU', 'Processor', 'Intel', 300.0)")
    connection.commit()
def dynamic_add_data(name, type, manufacturer, price):
    cursor.execute("INSERT INTO parts (name, type, manufacturer, price) VALUES (?, ?, ?, ?)", (name, type, manufacturer, price))
    connection.commit()
def show_data():
    cursor.execute("SELECT * FROM parts")
    data = cursor.fetchall()
    for row in data:
        print(row)
def dynamic_show_data(type):
    cursor.execute("SELECT name FROM parts WHERE type=?", (type,))
    data = cursor.fetchall()
    for row in data:
        print(row)
def update_name(old_name, new_name):
    cursor.execute("UPDATE parts SET name=? WHERE name=?", (new_name, old_name))
    connection.commit()
def update_manufacturer(old_manufacturer, new_manufacturer):
    cursor.execute("UPDATE parts SET manufacturer=? WHERE manufacturer=?", (new_manufacturer, old_manufacturer))
    connection.commit()
def delete_data(name):
    cursor.execute("DELETE FROM parts WHERE name=?", (name,))
    connection.commit()
create_table()
add_data()
dynamic_add_data('GPU', 'Graphics Card', 'NVIDIA', 500.0)
dynamic_add_data('RAM', 'Memory', 'Corsair', 150.0)
dynamic_add_data('SSD', 'Storage', 'Samsung', 200.0)
show_data()
print("Showing all Memory parts:")
dynamic_show_data('Memory')
update_name('RAM', 'RAM Memory')
update_manufacturer('Intel', 'AMD')
print("Updated Data:")
show_data()
delete_data('SSD')
print("Data after deletion:")
show_data()
connection.close()
