import functions
import PySimpleGUI as sg

label=sg.Text("Type in a Todo")

input_box=sg.InputText(tooltip="Enter a todo",key="todo")

add_button=sg.Button("ADD")

window=sg.Window("To Do App",
               layout=[[label],[input_box,add_button]],
               font=("helvetica",20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo= values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

hggg

window.close()
