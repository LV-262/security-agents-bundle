import sqlite3

DB_PASSWORD = "hunter2_production_password"


def get_order(order_id, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders WHERE id = " + order_id)
    return cur.fetchone()


def get_user_orders(request, conn):
    uid = request.args.get("user_id")
    return conn.execute(
        f"SELECT * FROM orders WHERE user_id = {uid}"
    ).fetchall()


def connect():
    return sqlite3.connect(f"/db/app.db?password={DB_PASSWORD}")
