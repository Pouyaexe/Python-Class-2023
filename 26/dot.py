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


task1 = Task("Eggs","Fresh")

number = 3

my_string = "abc"
my_string.upper()
print(type(task1))