# 📝 Python Todo App — MVC + MySQL

This is a beginner-friendly command-line **Todo App** built using:
- **Python 3**
- **MySQL (via MySQL Workbench)**
- **MVC Architecture**
- **Virtual Environment**
- **`.env` configuration**
- **UUID for unique Todo IDs**

---

## 📁 Project Folder Structure

```
python-db-todo-app/
│
├── config/              # DB connection + environment setup
│   └── config.py
│
├── controller/          # Logic layer (connects view ↔ model)
│   └── todo_controller.py
│
├── model/               # Data models and schema
│   └── todo_model.py
│
├── repository/          # SQL queries in separate files
│   └── schema_initializer.py
|   └── todo_repo.py
│
├── view/                # User input/output (console interface)
│   └── todo_view.py
│
├── .env                 # Secure DB credentials
├── main.py              # App entry point
└── README.md
```

---

## ⚙️ Features

- ✅ Add a new Todo
- 📋 Show all Todos
- 🔍 Get Todo by ID
- ✏️ Update Todo
- 🧪 Database connection check
- 💾 Auto-creates required table if not exists

---

## 🔐 `.env` Example

Create a `.env` file in the root with:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=todo_db
```

> 🛑 You must manually create the **`todo_db`** database in MySQL Workbench before running the app.

---

## 🧪 Testing the DB Connection

In `config/config.py`, the `test_db_connection()` function will check if DB is connected.

```python
# In main.py
from config.config import test_db_connection

test_db_connection()
```

If connected, you’ll see:
```
✅ Database connection successful.
```

---

## ▶️ How to Run

1. ✅ **Create virtual environment** (first time only):

   ```bash
   python -m venv venv
   ```

2. ▶️ **Activate virtual environment**:

   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

3. 🧩 **Install dependencies**:

   ```bash
   pip install mysql-connector-python python-dotenv
   ```

4. 🚀 **Run the app**:

   ```bash
   python main.py
   ```

---

## 📚 What Students Learn

- MVC architecture in real projects
- Environment variable usage with `.env`
- Modular Python coding
- MySQL integration and CRUD operations
- UUID for secure and unique identifiers

---

## ❤️ Contribution

This project is intended for learning purposes. Feel free to:
- Fork the repo
- Add new features (e.g., Delete Todo)
- Improve validations

---

## 📸 Maintainer

Built by **Muhammad Muneeb Saleem** 
---
