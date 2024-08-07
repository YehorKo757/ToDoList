from modules import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo",
                                    key="todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[[label], [input_box, add_button]],
                              font=("Helvetica", 16))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()