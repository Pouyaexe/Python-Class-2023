**Project Title: Interactive To-Do List Manager**

**Project Description:**
In this project, your students will create a command-line-based interactive to-do list manager. The program will allow users to add, edit, and remove tasks, mark tasks as completed, and view the current list of tasks. Each task will have a name, description, and status (completed or not).

**Features to Implement:**

1. **Getting Started:**

   - Display a welcome message and instructions on how to use the to-do list manager.
2. **Variables and Simple Data Types:**

   - Use appropriate variables to store tasks' information like name, description, and status.
3. **Lists:**

   - Create a list to store all the tasks.
   - Implement functionality to add new tasks to the list.
4. **Working with Lists:**

   - Allow users to view all the tasks in the list.
   - Implement the ability to edit the details of a task.
   - Allow users to mark a task as completed or not completed.
5. **If Statements:**

   - Handle invalid user inputs using if statements (e.g., when the user enters a non-existent task number).
6. **Dictionaries:**

   - Use dictionaries to store the details of each task (name, description, status) as key-value pairs.
7. **User Input and while Loops:**

   - Use a while loop to continuously prompt the user for actions until they choose to exit the program.
   - Provide options for adding, editing, and removing tasks.
8. **Functions:**

   - Implement functions for each action (e.g., add_task, edit_task, mark_completed) to make the code modular and organized.
9. **Classes:**

   - Create a `Task` class to encapsulate task-related data and methods.
   - Refactor the program to use the `Task` class to represent each task.

**Bonus Features (Optional):**

- Implement the ability to save and load the to-do list from a file, so users can keep their tasks between sessions.
- Add color-coding to distinguish between completed and uncompleted tasks in the list display.
- Allow users to sort the tasks based on name, status, or due date.
- Implement reminders for tasks with due dates.

**Explanation:**
The project focuses on creating a command-line-based to-do list manager using Python. It utilizes concepts from the chapters you taught your students in the class:

1. **Getting Started:** Display a welcome message and instructions to guide users on using the program.
2. **Variables and Simple Data Types:** Use variables to store the information related to each task, such as name, description, and status (completed or not).
3. **Lists:** Create a list to store all the tasks. This list will be used to perform various operations on tasks.
4. **Working with Lists:** Allow users to view the current list of tasks. Provide functionality to edit task details and mark tasks as completed or not completed.
5. **If Statements:** Use if statements to handle invalid user inputs gracefully, ensuring that the program doesn't crash when receiving unexpected inputs.
6. **Dictionaries:** Use dictionaries to store the details of each task. This allows us to organize the data for each task with meaningful key-value pairs.
7. **User Input and while Loops:** Use a while loop to repeatedly prompt the user for actions until they choose to exit the program. This ensures a user-friendly experience.
8. **Functions:** Implement functions for each action to keep the code modular and organized. Functions like `add_task`, `edit_task`, and `mark_completed` help in managing the tasks.
9. **Classes:** Create a `Task` class to represent each task as an object. This encapsulates the data and methods related to a task and promotes code reusability.

**Bonus Features (Optional):**

- For the bonus features, we'll provide separate solutions below.

**Solving the Bonus Features: ⭐**

1. **Save and Load the To-Do List from a File:**
   To implement this feature, you can add functions to save the current list of tasks to a file and load it back when the program starts. You can use Python's built-in `open` function to write and read the task data to/from a file in a structured format (e.g., JSON or CSV).
2. **Add Color-Coding to Distinguish Completed Tasks:**
   To add color-coding to the display, you can use a Python library like `colorama` or `termcolor`. These libraries allow you to add color and styling to the text printed in the command-line interface. For example, you can display completed tasks in green and uncompleted tasks in red.
3. **Allow Users to Sort Tasks:**
   To implement sorting, you can provide options to sort tasks based on different criteria (e.g., name, status, or due date). You can use Python's `sorted` function with a custom sorting key to sort the tasks accordingly.
4. **Implement Reminders for Tasks with Due Dates:**
   For tasks with due dates, you can add a due date attribute to the `Task` class. Then, you can implement a reminder feature that checks the due date of each task and reminds the user of upcoming or overdue tasks when the program starts.

Each of these bonus features can be tackled individually, and they provide opportunities for your students to expand their project's functionality and demonstrate their Python skills. Encourage them to be creative and explore additional features that can make their to-do list manager more user-friendly and efficient.

## Sample Output

```plaintext
--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 1
Enter the task name: Buy groceries
Enter the task description: Milk, eggs, bread
Task added successfully!

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 1
Enter the task name: Clean the house
Enter the task description: Vacuum, dusting
Task added successfully!

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 4
To-Do List:
1. Buy groceries - Milk, eggs, bread [Not Completed]
2. Clean the house - Vacuum, dusting [Not Completed]

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 3
Enter the task index to mark as completed: 1
Task marked as completed!

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 4
To-Do List:
1. Buy groceries - Milk, eggs, bread [Completed]
2. Clean the house - Vacuum, dusting [Not Completed]

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 2
Enter the task index to edit: 2
Enter the new task name: Clean the house
Enter the new task description: Vacuum, dusting, mop
Task updated successfully!

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 4
To-Do List:
1. Buy groceries - Milk, eggs, bread [Completed]
2. Clean the house - Vacuum, dusting, mop [Not Completed]

--- To-Do List Manager ---
1. Add Task
2. Edit Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice (1-5): 5
Exiting the To-Do List Manager.

```
