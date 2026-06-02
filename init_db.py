import sqlite3

def init_database():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
    ''')
    cursor.execute('DELETE FROM products')

    products_data = [
        ("Игровая консоль", 250000, "Современная игровая приставка для гейминга в 4K.", "/static/images/console.png"),
        ("Беспроводные наушники", 85000, "Наушники с активным шумоподавлением и чистым звуком.", "/static/images/headphones.png"),
        ("Механическая клавиатура", 45000, "RGB подсветка, синие свичи, идеальный отклик.", "/static/images/keyboard.png"),
        ("Ноутбук", 450000, "Мощный ноутбук для работы, учебы и программирования.", "/static/images/laptop.png"),
        ("Монитор", 120000, "27-дюймовый IPS монитор с частотой обновления 144 Гц.", "/static/images/monitor.png"),
        ("Компьютерная мышь", 25000, "Игровая эргономичная мышь с высоким DPI.", "/static/images/mouse.png"),
        ("Смартфон", 350000, "Флагманский смартфон с отличной камерой и экраном 120 Гц.", "/static/images/phone.png"),
        ("Умные часы", 95000, "Стильные часы с мониторингом пульса, сна и тренировок.", "/static/images/smartwatch.png"),
        ("Портативная колонка", 35000, "Влагозащищенная колонка с мощным басом.", "/static/images/speaker.png"),
        ("Планшет", 220000, "Тонкий планшет с поддержкой стилуса для рисования и заметок.", "/static/images/tablet.png")
    ]

    cursor.executemany('''
        INSERT INTO products (name, price, description, image_url)
        VALUES (?, ?, ?, ?)
    ''', products_data)

    conn.commit()
    conn.close()
    print("База данных успешно создана и наполнена 10 товарами!")

if __name__ == '__main__':
    init_database()