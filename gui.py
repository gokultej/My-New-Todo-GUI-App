import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('',key='clock')
label=sg.Text("Type in a Todo")
#add button instructions
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
add_button=sg.Button("Add",size=10)
#edit button instructions
list_box=sg.Listbox(values=functions.get_todos(),key="todos",
                    enable_events=True, size=[45,10])

edit_button=sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window=sg.Window("To Do App",
               layout = [[clock],
                         [label] ,
                         [input_box,add_button],
                         [list_box,edit_button,delete_button],
                         [exit_button]],
               font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo= values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select An Option")
        case "Delete":
            try:
                todo_to_delete=values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please Select An Option")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
