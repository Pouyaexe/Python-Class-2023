class Task:
    def __init__(self, name) -> None:
        self.name = name 
        self.is_star = False 
        self.is_completed = False 

  

task1 = Task("milk")

task2 = Task("eggs")


todo_list = []

todo_list.append(task1)
todo_list.append(task2)

def find_and_complete(todolist):
    for task in todo_list:
        if task.name == "milk":
            task.is_star == True
    return todo_list

        
# print(todo_list)

task1.task_complete()

print(task1.is_completed)



todo_list_2 = []

task3 = "Buying Milk"
task4 = "Studying"

todo_list_2.append(task3)
todo_list_2.append(task4)

def task_func(todolist:list, newtask:str):
    todolist.append(newtask)
    return todolist

print(todo_list_2)