user_prompt = "Type add {todo}, show, edit {number in list}, complete {number in list} or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.lower().startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            print(f"{index+1}. {todo}", end='')

    elif user_action.lower().startswith("edit"):
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number_to_edit = int(user_action[5:])
            check = todos[number_to_edit - 1]  # Check for IndexError (input is higher than last index in list)
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ") + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Please, enter number of todo to edit")
            continue
        except IndexError:
            print("Number is out of a range available in a list")
            continue

    elif user_action.lower().startswith("complete"):
        try:
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number_to_complete = int(user_action[9:])
            todo_to_remove = todos[number_to_complete - 1]
            todos.remove(todo_to_remove)  # can also use todos.pop(number_to_complete - 1)
            message_complete = f"Todo {todo_to_remove} was removed from the list.".replace("\n", " ", 1)
            print(message_complete)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
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
