user_prompt = "Type add, show, edit or exit: "
todos = []

while True:
    user_action = input(user_prompt)

    match user_action.strip():
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'edit':
            number = int(input("What number of todo you want to edit? "))
            todos[number-1] = input(f"Reenter number {number} todo: ")
        case 'exit':
            print('Bye!')
            break
        case _:
            print("Hey, you've entered a wrong command")
