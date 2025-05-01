# 📝 Docker To-Do App with .env Config

This is a simple Flask-based To-Do app that uses Docker and a `.env` file to handle configuration like **port numbers** and **database paths** — making it clean, flexible, and more production-ready.

---

## 💡 Why I Built This

I wanted to get more practice with Docker volumes, live editing using bind mounts, and especially how to use `.env` files to manage configuration the right way.

---

## ✅ Key Features

- Flask web app with a simple task list
- Uses SQLite as a lightweight database
- Docker volume for persistent DB storage
- Bind mount for live HTML editing
- `.env` file controls:
  - Port number (`PORT`)
  - DB location (`DB_PATH`)
- Tested by changing ports between `5000` and `5001` in the `.env` file without touching any code

---

## ⚙️ .env File Example

```env
PORT=5001
DB_PATH=/data/todo.db
```

## 🐳 How to Run

1. Clone the repo

2. Edit .env to set your port or DB path

3. Build and run with Docker Compose:

```bash
docker-compose up --build
```

Then open your browser to:
http://localhost:5001

## 📦 Tech Stack

- Python 3.11
- Flask
- SQLite
- Docker
- Docker Compose
- Bootstrap 5
