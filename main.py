def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file.
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


user_prompt = "Type add {todo}, show, edit {number in list}, complete {number in list} or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.lower().startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            print(f"{index+1}. {todo}", end='')

    elif user_action.lower().startswith("edit"):
        try:
            todos = get_todos()

            number_to_edit = int(user_action[5:])
            check = todos[number_to_edit - 1]  # Check for IndexError (input is higher than last index in list)
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ") + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please, enter number of todo to edit")
            continue
        except IndexError:
            print("Number is out of a range available in a list")
            continue

    elif user_action.lower().startswith("complete"):
        try:
            todos = get_todos()

            number_to_complete = int(user_action[9:])
            todo_to_remove = todos[number_to_complete - 1]
            todos.remove(todo_to_remove)  # can also use todos.pop(number_to_complete - 1)
            message_complete = f"Todo {todo_to_remove} was removed from the list.".replace("\n", " ", 1)
            print(message_complete)

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please, enter number of todo to complete")
            continue
        except IndexError:
            print("Number is out of a range available in a list")
            continue

    elif user_action.lower().startswith("exit"):
        print('Bye!')
        break
    else:
        print("Hey, you've entered a wrong command")
