user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show':
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}", end='')

        case 'edit':
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number_to_edit = int(input("What number of todo you want to edit? "))
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ") + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number_to_complete = int(input("What number of todo you want to complete? "))
            todo_to_remove = todos[number_to_complete - 1]
            todos.remove(todo_to_remove)  # can also use todos.pop(number_to_complete - 1)
            message_complete = f"Todo {todo_to_remove} was removed from the list.".replace("\n", " ", 1)
            print(message_complete)
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'exit':
            print('Bye!')
            break
        case _:
            print("Hey, you've entered a wrong command")
