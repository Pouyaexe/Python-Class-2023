class Task:
    def __init__(self,name, description, status = False) -> None:
        self.name = name
        self.description = description
        self.status = status
        
    def mark_completed(self):
        self.status = True
    
    def update_name(self):
        self.name = input("Enter the new name: ")
        self.description = input("Enter the new description: ")
        
    def __repr__(self) -> str:
        if self.status:
            return self.name + " - "+ self.description + " [(Completed)]"
        else:
            return self.name + " - "+ self.description + " [(Not Completed)]"    

tasks = []

while True:
    if len(tasks) > 0:   
        print("--- ToDOs: ---")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        
    print("--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")
    
    choice = input("Enter your choice(1-5): ")
    
    if choice == "1":
        name = input("Enter the task name: ")
        desc = input("Input the description: ")
        tasks.append(Task(name, desc))
        print("Task added successfully!")
    
    # elif choice == "2":
    #     index = int(input("Enter the task index to edit: ")) - 1
    #     new_name = input("Enter the new task name: ")
    #     new_desc = input("Enter the new task description: ")
    #     task[index].name = new_name
    #     task[index].description = new_desc
    #     print("Task Updated seuccessfully!")
    
    elif choice == "2": 
        index = int(input("Enter the task index to edit: ")) - 1
        tasks[index].update_name()
        print("Task Updated seuccessfully!")
        
    elif choice == "3":
        index = int(input("Enter the task index to complete: ")) - 1
        tasks[index].mark_completed()
        print(f"Task {index + 1} marked as completed")
    
    elif choice == "4":
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
            
    elif choice == "5":
        print("Exiting the To-Do List Manager.")
        break
    