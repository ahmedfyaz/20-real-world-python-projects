def get_todos():
    with open("todos.txt",'r')as file :
        todos = file.readlines()
    return todos
def add_todos(todos):
    with open("todos.txt",'w')as file:
        file.writelines(todos)
def show_todos(todos):
    for index,todo in enumerate(todos):
        print(f"{index+1}-> {todo.strip("\n")}")

    
while True:
    user_input = input("Select Your Action 'add','edit','completed','show' 'exit' : ").lower().strip()
    if(user_input.startswith('add')):
        try:
            todo = input("Enter your todo : ")+"\n"
            todos = get_todos()
            todos.append(todo)
            add_todos(todos)    
        except ValueError:
            print("Your command is invalid")        
    
    elif(user_input.startswith('show')):
        try:
            todos = get_todos()
            show_todos(todos)
        except ValueError:
            print("Your command is invalid")
    elif(user_input.startswith('edit')):
        try:
            todos = get_todos()
            show_todos(todos)
            number = int(input("Enter number of the todo"))
            number = number-1
            edited_todo = input("Enter new todo")
            todos[number] = edited_todo + "\n"
            add_todos(todos)
        except ValueError:
            print("Your command is invalid")
    elif(user_input.startswith('completed')):
        try:
            todos = get_todos()
            show_todos(todos)
            number = int(input("Write the number of todo that is completed"))
            todos.pop(number-1)
            add_todos(todos)
        except ValueError:
            print("Your command is invalid")        
    elif(user_input.startswith('exit')):
        break
    else:
        print(f"{user_input} dont exist")
print("GoodBye")