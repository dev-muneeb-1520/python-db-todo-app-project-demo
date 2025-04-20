from controllers.todo_controller import TodoController
from repository.schema_initializer import create_table
from config.db_config import testDBConnection
        
def main():
    testDBConnection()  
    create_table()
    controller = TodoController()

    while True:
        print("\n1. Add Todo\n2. List Todos\n3. Get Todo by ID\n4. Update Todo\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            controller.addTodo()
        elif choice == "2":
            controller.listTodos()
        elif choice == "3":
            controller.get_todo_by_id()
        elif choice == "4":
            controller.update_todo()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
    
    