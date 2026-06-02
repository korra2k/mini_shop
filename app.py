from flask import Flask, render_template, abort
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('shop.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    
    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>')
def product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    
    if product is None:
        abort(404)
        
    return render_template('product.html', product=product)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)