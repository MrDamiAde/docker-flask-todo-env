from flask import Flask, render_template, request, redirect
import os
import sqlite3

app = Flask(__name__)

DB_PATH = os.environ.get("DB_PATH", "/data/todo.db")  


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    init_db()

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("INSERT INTO todos (task) VALUES (?)", (task,))
            conn.commit()
            conn.close()
        return redirect("/")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, task FROM todos")
    todos = c.fetchall()
    conn.close()
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
