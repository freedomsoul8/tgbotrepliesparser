import sqlite3

conn = sqlite3.connect('db.db',check_same_thread=False)
cursor = conn.cursor()

def create_table_products():
    sql = "CREATE TABLE products(id text, root text, size text)"
    cursor.execute(sql)
    conn.commit()

def save_product(root,id,size):
    sql = "INSERT INTO products(id,root,size) VALUES(?,?,?)"
    values = (id,root,size)
    cursor.execute(sql,values)
    conn.commit()
    return

def select_product_data():
    sql = "SELECT id,root,size FROM products"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def create_table_links():
    sql = "CREATE TABLE links(url text)"
    cursor.execute(sql)
    conn.commit()
    return

def save_link(url):
    sql = "INSERT INTO links(url) VALUES(?)"
    values = (url,)
    cursor.execute(sql,values)
    conn.commit()
    return

def select_links():
    sql = "SELECT url FROM links"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def create_table_fb():
    sql = "CREATE TABLE feedbacks(fb_text text, url text)"
    cursor.execute(sql)
    conn.commit()
    return

def save_feedback(text,url):
    sql = "INSERT INTO feedbacks(fb_text, url) VALUES(?,?)"
    values = (text,url)
    cursor.execute(sql,values)
    conn.commit()
    return

def select_feedbacks():
    sql = "SELECT fb_text,url FROM feedbacks"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def clear_table_fb():
    sql = "DELETE FROM feedbacks"
    cursor.execute(sql)
    conn.commit()
    return



def clear_table_links():
    sql = "DELETE FROM links"
    cursor.execute(sql)
    conn.commit()
    return

def clear_table_prod():
    sql = "DELETE FROM products"
    cursor.execute(sql)
    conn.commit()
    return