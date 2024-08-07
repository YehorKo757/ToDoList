from modules import functions

user_prompt = "Type add {todo}, show, edit {number in list}, complete {number in list} or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.lower().startswith("show"):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            print(f"{index+1}. {todo}", end='')

    elif user_action.lower().startswith("edit"):
        try:
            todos = functions.get_todos()

            number_to_edit = int(user_action[5:])
            check = todos[number_to_edit - 1]  # Check for IndexError (input is higher than last index in list)
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ") + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please, enter number of todo to edit")
            continue
        except IndexError:
            print("Number is out of a range available in a list")
            continue

    elif user_action.lower().startswith("complete"):
        try:
            todos = functions.get_todos()

            number_to_complete = int(user_action[9:])
            todo_to_remove = todos[number_to_complete - 1]
            todos.remove(todo_to_remove)  # can also use todos.pop(number_to_complete - 1)
            message_complete = f"Todo {todo_to_remove} was removed from the list.".replace("\n", " ", 1)
            print(message_complete)

            functions.write_todos(todos)
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
