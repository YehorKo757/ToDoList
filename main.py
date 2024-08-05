user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                print(f"{index+1}. {todo}", end='')
        case 'edit':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number_to_edit = int(input("What number of todo you want to edit? "))
            todos[number_to_edit - 1] = input(f"Reenter number {number_to_edit} todo: ")

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'complete':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number_to_complete = int(input("What number of todo you want to complete? "))
            todos.remove(todos[number_to_complete - 1])
            
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'exit':
            print('Bye!')
            break
        case _:
            print("Hey, you've entered a wrong command")
