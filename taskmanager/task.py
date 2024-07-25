# Create class for task.

class Task:
#__init__: Este es el constructor de la clase. Se llama automáticamente cuando se crea una nueva instancia de la clase. Inicializa los atributos description, due_date y completed.    
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

#mark_complete: Este método cambia el estado de la tarea a completada.
    def mark_complete(self):
        self.completed = True

#__str__: Este método define cómo se debe representar la tarea cuando se convierte a una cadena (por ejemplo, cuando se imprime). Muestra una descripción legible de la tarea.
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.description}, Due Date: {self.due_date}, Status: {status}"
#TaskManager sera la lista de metodos.
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, due_date):
        task = (description, due_date)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")
    
    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
#main: Esta función muestra el menú y procesa la elección del usuario. Dependiendo de la opción elegida, llama a los métodos correspondientes en TaskManager.
def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5) ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            manager.add_task(description, due_date)
            print("Task added succesfully.")
        elif choice == "2":
            manager.list_tasks()
            index = int(input("Enter task number to mark as complete: "))
            manager.list_tasks(index)
            print("Task completed")
        elif choice == "3":
            manager.list_tasks()
            index = int(input("Enter task number to remove: "))
            manager.remove_task(index)
            print("Task removed")
        elif choice == "4":
            print("Tasks list: \n")
            manager.list_tasks()
        elif choice == "5":
            print("Exiting... ")
            break
        else:
            print("Enter a valid option: ")
#if __name__ == "__main__":: Esto asegura que main() solo se ejecute si el archivo es ejecutado directamente, y no si es importado como un módulo en otro archivo.
if __name__ == "__main__":
    main()