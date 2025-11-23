import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in Todo")
input_text = sg.InputText(tooltip="Enter Todo",key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
del_button = sg.Button("Completed")
exit_button = sg.Button("Exit")
show_button = sg.Button("Show")

window = sg.Window("My Todo-App",layout=[[label],[input_text,add_button,edit_button,del_button,show_button,exit_button]],font=('Helvetica',20))

while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.add_todos("todos.txt",todos)
        case sg.WIN_CLOSED:
            break
window.close()