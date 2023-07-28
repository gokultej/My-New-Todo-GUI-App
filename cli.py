import time
import functions

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is :",now)

while True:
    User_action = input("enter add (or)show(or)edit(or)delete(or)exit")
    User_action = User_action.strip()
#strip function is used to remove spaces in the input
    if User_action.startswith("add"):
        Todo = User_action[4:]

        todos=functions.get_todos()


        todos.append(Todo + "\n")

        functions.write_todos(todos)


    elif User_action.startswith("show"):
        todos=functions.get_todos()


        # new_todos = [item.strip for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}---{item}"
            print(row)
    elif  User_action.startswith("edit"):
        try:
            number = int(User_action[5:])
            print(number)
            number = number - 1
            todos=functions.get_todos()


            new_todo = input("enter new todo:")
            todos[number] = new_todo +'\n'


            functions.write_todos(todos)
        except ValueError:
            print("Add should'nt be at first off the line")
            continue

    elif  User_action.startswith("delete"):
        try:
            number = int(User_action[7:])
            todos=functions.get_todos()

            index = number -1
            todo_to_remove = todos[index].strip("\n")
            a = todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was Removed from the list"
            print(message)
        except IndexError:
            print("Enter the valid correct value present in the List")
            continue

    elif User_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye!")

