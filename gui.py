from modules import functions
import FreeSimpleGUI
import time

FreeSimpleGUI.theme("Dark")

clock = FreeSimpleGUI.Text("", key="clock")
label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo",
                                    key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(),
                                 key="todos",
                                 enable_events=True,
                                 size=(45, 10))
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = FreeSimpleGUI.Window("My To-Do App",
                              layout=layout,
                              font=("Helvetica", 16))

while True:
    event, values = window.read(timeout=200)
    # Check for event of closing window should be just after event registration
    if event == FreeSimpleGUI.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first",
                                    font=("Helvetica", 16))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first", font=("Helvetica", 16))
        case "todos":
            try:
                window["todo"].update(value=values["todos"][0].strip("\n"))
            except IndexError:
                continue
        case "Exit":
            break

window.close()
