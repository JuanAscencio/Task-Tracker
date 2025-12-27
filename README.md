# Task Tracker

Task tracker is a project used to track and manage your task. <br>
In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done and what you are currently working on. <br>

---

## Requirements

The aplication should run from the command line, accept user actions and inputs as arguments, and sotre the task in a JSON file. <br>
The user should be able to: <br>

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

Here are come constraints to guide the implementation

- You can use any programming language to build this project.
- Use positional arguments in command line to accept user inputs.
- Use a JSON file to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the native file system module of your programming language to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Ensure to handle errors and edge cases gracefully.

---

## Example

The list of commands and their usage is given below: <br>

```bash:
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```
