from repository.todo_repo import TodoRepo
from views.todo_view import TodoView
from models.todo_model import Todo

class TodoController:
  def __init__(self):
    self.repo = TodoRepo()
    self.view = TodoView()
    
  def addTodo(self):
    title, completed = self.view.get_todo_input()
    todo = Todo(title=title, completed=completed)
    self.repo.addTodo(todo)
    print("✅ Todo added successfully.")
    
  def listTodos(self):
    todos = self.repo.getTodo()
    self.view.show_todos(todos)

  def get_todo_by_id(self):
      todo_id = self.view.get_todo_id_input()
      todo = self.repo.getTodoById(todo_id)
      self.view.show_todo(todo)

  def update_todo(self):
      todo_id = self.view.get_todo_id_input()
      title, completed = self.view.get_update_input()
      self.repo.updateTodoById(todo_id, title, completed)
      print("✅ Todo updated successfully.")