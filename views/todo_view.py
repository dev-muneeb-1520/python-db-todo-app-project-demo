class TodoView:
  # show all todos
  def show_todos(self, todos):
    print("\n--- Todo List ---")
    for todo in todos:
        status = "✅" if todo.completed else "❌"
        print(f"{todo.id} | {todo.title} - {status}")
    print("------------------")

  # create todo
  def get_todo_input(self):
    title = input("Enter todo title: ")
    completed_input = input("Is the todo completed? (yes/no): ").strip().lower()
    completed = True if completed_input == "yes" else False
    return title, completed

  # input id to get the specific todo by id
  def get_todo_id_input(self):
      return input("Enter the Todo ID: ").strip()

  # update todo
  def get_update_input(self):
      title = input("Enter new title: ")
      completed_input = input("Is it completed? (yes/no): ").strip().lower()
      completed = True if completed_input == "yes" else False
      return title, completed
    
  # show todo by id
  def show_todo(self, todo):
      if todo:
          status = "✅" if todo.completed else "❌"
          print(f"\n{todo.id} | {todo.title} - {status}")
      else:
          print("❌ Todo not found.")