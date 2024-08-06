user_prompt = "Type add {todo}, show, edit {number in list}, complete {number in list} or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            print(f"{index+1}. {todo}", end='')

    elif 'edit' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number_to_edit = int(user_action[5:])
        todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ") + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number_to_complete = int(user_action[9:])
        todo_to_remove = todos[number_to_complete - 1]
        todos.remove(todo_to_remove)  # can also use todos.pop(number_to_complete - 1)
        message_complete = f"Todo {todo_to_remove} was removed from the list.".replace("\n", " ", 1)
        print(message_complete)
            
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'exit' in user_action:
        print('Bye!')
        break
    else:
        print("Hey, you've entered a wrong command")
