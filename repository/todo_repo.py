from config.db_config import connectToDB
from models.todo_model import Todo

class TodoRepo: 
  def addTodo(self, todo: Todo):
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute(
      "Insert into todos (id, title, completed) values (%s, %s, %s)",
      (todo.id, todo.title, todo.completed)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
  
  def getTodo(self):
    conn = connectToDB()
    cursor = conn.cursor()
    cursor.execute(
      "Select id, title, completed from todos"
    )
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return [Todo(id=row[0], title=row[1], completed=bool(row[2])) for row in rows]
    
  def getTodoById(self, todo_id):
      conn = connectToDB()
      cursor = conn.cursor()
      cursor.execute("SELECT id, title, completed FROM todos WHERE id = %s", (todo_id,))
      row = cursor.fetchone()
      cursor.close()
      conn.close()

      if row:
          return Todo(id=row[0], title=row[1], completed=bool(row[2]))
      return None

  def updateTodoById(self, todo_id, title, completed):
      conn = connectToDB()
      cursor = conn.cursor()
      cursor.execute("UPDATE todos SET title = %s, completed = %s WHERE id = %s",
                      (title, completed, todo_id))
      conn.commit()
      cursor.close()
      conn.close()